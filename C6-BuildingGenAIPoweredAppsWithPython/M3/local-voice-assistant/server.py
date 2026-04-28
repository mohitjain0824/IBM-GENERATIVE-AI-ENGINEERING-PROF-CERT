from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from worker import speech_to_text, local_llm_process, text_to_speech
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-voice', methods=['POST'])
def process_voice():
    # Save the incoming audio blob
    audio_file = request.files['audio']
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)

    # 1. Speech to Text
    user_text = speech_to_text(audio_path)
    
    # 2. Local LLM Response
    ai_response = local_llm_process(user_text)
    
    # 3. Text to Speech
    audio_response_path = text_to_speech(ai_response)
    
    return jsonify({
        "userText": user_text,
        "aiResponse": ai_response,
        "audioUrl": "/static/response.mp3"
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)