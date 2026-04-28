import pyttsx3
import requests
from faster_whisper import WhisperModel
import os

# Initialize STT Model (Fastest local version)
stt_model = WhisperModel("tiny", device="cpu", compute_type="int8")

def speech_to_text(audio_path):
    segments, _ = stt_model.transcribe(audio_path)
    text = " ".join([segment.text for segment in segments])
    return text

def local_llm_process(user_message):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",
        "prompt": f"Act as a helpful voice assistant. Keep responses short (1-2 sentences). User says: {user_message}",
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json().get('response', "I'm having trouble thinking.")

def text_to_speech(text, output_path="static/response.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path