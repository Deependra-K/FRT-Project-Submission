import os
import numpy as np
import pandas as pd
import wave
import librosa
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

app = Flask(__name__)

# Load dataset
data = pd.read_csv("voice.csv")  # Assuming the dataset is stored in a file called "voice.csv"

# Convert categorical labels into numerical labels
data['label'] = data['label'].map({'male': 0, 'female': 1})

# Extract features and labels
X = data.drop('label', axis=1)
y = data['label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define the Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the final model
final_model = rf.fit(X_train_scaled, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = "uploaded_audio.wav"
        file.save(filename)
        gender = predict_gender(filename)
        os.remove(filename)
        return jsonify(gender=gender)

def extract_features(filename):
    y, sr = librosa.load(filename, sr=None)  # Load audio file

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)  # Using 20 MFCC coefficients
    mfccs_mean = np.mean(mfccs, axis=1)  # Calculate the mean of MFCC coefficients
    return mfccs_mean.reshape(1, -1)  # Return the feature vector as a 2D array

def predict_gender(filename, threshold=0.5):
    # Extract features from audio file
    features = extract_features(filename)

    # Scale the features
    features_scaled = scaler.transform(features)

    # Use the final model to predict gender and obtain probabilities
    probabilities = final_model.predict_proba(features_scaled)

    # Make the final prediction based on probabilities and custom threshold
    if probabilities[0, 0] > threshold:
        return "Male"
    else:
        return "Female"

if __name__ == "__main__":
    app.run(debug=True)
