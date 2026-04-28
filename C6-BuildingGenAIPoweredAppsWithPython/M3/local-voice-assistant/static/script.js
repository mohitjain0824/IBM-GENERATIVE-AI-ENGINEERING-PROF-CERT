let mediaRecorder;
let audioChunks = [];
const recordBtn = document.getElementById('record-btn');
const chatBox = document.getElementById('chat-box');
const audioPlayer = document.getElementById('audio-player');

recordBtn.addEventListener('click', async () => {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        recordBtn.innerText = "🎤 Start Recording";
        recordBtn.classList.remove('recording');
    } else {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);
        audioChunks = [];

        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
            sendToBackend(audioBlob);
        };

        mediaRecorder.start();
        recordBtn.innerText = "🛑 Stop Recording";
        recordBtn.classList.add('recording');
    }
});

async function sendToBackend(blob) {
    const formData = new FormData();
    formData.append('audio', blob, 'recording.wav');

    chatBox.innerHTML += `<p><strong>You:</strong> ...processing voice...</p>`;

    try {
        const response = await fetch('/process-voice', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();
        
        // Update UI with text
        chatBox.innerHTML += `<p><strong>User:</strong> ${data.userText}</p>`;
        chatBox.innerHTML += `<p><strong>AI:</strong> ${data.aiResponse}</p>`;
        
        // Play AI Voice
        audioPlayer.src = data.audioUrl + "?t=" + new Date().getTime(); // Prevent caching
        audioPlayer.play();
        
    } catch (error) {
        console.error("Error communicating with backend:", error);
        chatBox.innerHTML += `<p style="color:red;">Error processing voice.</p>`;
    }
}