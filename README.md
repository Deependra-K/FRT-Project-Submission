# FRT-Project-Submission

# Voice Gender Prediction Web Application

This project is a web application that records a user's voice, processes the audio to extract features, and predicts the gender of the speaker using a pre-trained machine learning model.

## Features
- Record audio from the user's microphone.
- Process the audio to extract MFCC features.
- Predict the gender of the speaker using a Random Forest classifier.
- Display the prediction result on the webpage.

## Requirements
- Python 3.x
- Flask
- NumPy
- Pandas
- Scikit-learn
- Librosa
- PyAudio

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/voice-gender-prediction.git
    cd voice-gender-prediction
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have the required audio packages installed:**
    ```bash
    sudo apt-get install portaudio19-dev   # For Debian-based systems
    brew install portaudio                 # For macOS with Homebrew
    ```

5. **Install PyAudio:**
    ```bash
    pip install pyaudio
    ```

## Dataset

Make sure you have a CSV file named `voice.csv` in the project directory. This dataset should contain voice features and labels for training the machine learning model.

## Running the Application

1. **Start the Flask application:**
    ```bash
    python app.py
    ```

2. **Open a web browser and navigate to:**
    ```
    http://127.0.0.1:5000/
    ```

## Project Structure

voice-gender-prediction/
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
├── css/
│ └── style.css
└── js/
└── script.js
├── voice.csv



- `app.py`: The main Flask application file.
- `requirements.txt`: List of required Python packages.
- `templates/index.html`: HTML template for the web page.
- `static/css/style.css`: CSS file for styling the web page.
- `static/js/script.js`: JavaScript file for handling audio recording and interaction with the backend.
- `voice.csv`: The dataset file containing voice features and labels.

## Usage

1. **Record Your Voice:**
   - Click the "Record" button to start recording.
   - Click the "Stop" button to stop recording.

2. **Get Prediction:**
   - After stopping the recording, the audio is sent to the server.
   - The server processes the audio, predicts the gender, and displays the result on the webpage.

## Troubleshooting

- Ensure your microphone is working and the browser has permission to access it.
- Check the console output for any errors during recording or prediction.
- Make sure all required packages are installed and up to date.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- The dataset used for training the model should be credited to its original source.
- Libraries and frameworks: Flask, Scikit-learn, Librosa, PyAudio.
