from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
import base64
import os
from worker import speech_to_text, ollama_process_message, text_to_speech

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def stt_route():
    audio_file = request.files['audio']
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)
    
    text = speech_to_text(audio_path)
    return jsonify({'text': text})

@app.route('/process-message', methods=['POST'])
def process_route():
    user_message = request.json.get('userMessage')
    
    # Get translation from Ollama
    translated_text = ollama_process_message(user_message)
    
    # Convert translation to speech
    speech_file = "response.mp3"
    text_to_speech(translated_text, speech_file)
    
    # Read speech file and encode to base64
    with open(speech_file, "rb") as f:
        audio_encoded = base64.b64encode(f.read()).decode('utf-8')
    
    return jsonify({
        "watsonxResponseText": translated_text, 
        "watsonxResponseSpeech": audio_encoded
    })

if __name__ == '__main__':
    app.run(port=8000, debug=True)