import whisper
import requests
import os
import pyttsx3

# initialize stt model
stt_model = whisper.load_model("base")

# initialize tts engine
tts_engine = pyttsx3.init()

def speech_to_text(audio_path):
    """Converts local audio files to text using whisper"""
    result = stt_model.transcribe(audio_path, fp16=False)
    return result['text']

def ollama_process_message(user_message):
    """Sends text to local Ollama/Llama3 for translation"""
    prompt=f"""
    Translate the following english sentence in to Hindi.
    Reply only with the translation. No explanation. No formatting. No extra text.ollama_process_message

    English: {user_message}
    Hindi: """

    response = requests.post('http://localhost:11434/api/generate',
                             json={
                                 "model": "llama3",
                                 "prompt": prompt,
                                 "stream": False
                             })
    return response.json().get('response', '').strip()

def text_to_speech(text, output_path):
    """Converts text to speech and saves to a file."""
    tts_engine.save_to_file(text, output_path)
    tts_engine.runAndWait()
    return output_path