let recorder, audio_stream;

document.getElementById('recordButton').onclick = async function() {
    audio_stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    recorder = new MediaRecorder(audio_stream);
    let chunks = [];

    recorder.ondataavailable = function(e) {
        chunks.push(e.data);
    };

    recorder.onstop = function() {
        const blob = new Blob(chunks, { type: 'audio/wav' });
        chunks = [];
        const formData = new FormData();
        formData.append('file', blob, 'audio.wav');

        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('status').textContent = 'Recording stopped';
            document.getElementById('result').textContent = `Predicted gender: ${data.gender}`;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('status').textContent = 'Error during prediction';
        });

        audio_stream.getTracks().forEach(track => track.stop());
    };

    recorder.start();
    document.getElementById('status').textContent = 'Recording...';
    document.getElementById('stopButton').disabled = false;
    document.getElementById('recordButton').disabled = true;
};

document.getElementById('stopButton').onclick = function() {
    recorder.stop();
    document.getElementById('stopButton').disabled = true;
    document.getElementById('recordButton').disabled = false;
};
