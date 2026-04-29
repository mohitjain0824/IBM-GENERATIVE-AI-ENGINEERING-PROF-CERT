# Local Babel Fish: Voice Translation Assistant

A 100% local, private, and free voice translation assistant inspired by Douglas Adams' *The Hitchhiker's Guide to the Galaxy*. This project converts speech to text, translates it into a target language using a Large Language Model (LLM), and speaks the result back to you—all running on your own hardware.

## 🚀 Features
- **Privacy-First:** No data leaves your machine. No cloud APIs, no tracking.
- **Speech-to-Text (STT):** Powered by OpenAI's **Whisper** (running locally).
- **LLM Translation:** Powered by **Ollama (Llama 3)**.
- **Text-to-Speech (TTS):** Powered by **pyttsx3**.
- **Web Interface:** A simple, responsive Flask-based frontend.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI Models:**
  - [Ollama](https://ollama.ai/) (Llama 3)
  - [OpenAI Whisper](https://github.com/openai/whisper)
- **Audio Processing:** FFmpeg
- **Frontend:** HTML5, JavaScript, CSS3

## 📋 Prerequisites
Before running the project, ensure you have the following installed:
1. **Python 3.10+**
2. **Ollama:** Download and install from [ollama.com](https://ollama.com/).
   - Pull the Llama 3 model: `ollama pull llama3`
3. **FFmpeg:** Required by Whisper for audio processing.
   - Ensure it is added to your System PATH.

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/local-language-translator.git
   cd local-language-translator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\\venv\\Scripts\\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask flask-cors requests openai-whisper pyttsx3
   ```

## 🏃 How to Run

1. **Start Ollama:** Ensure the Ollama service is running in the background.
2. **Run the Flask server:**
   ```bash
   python server.py
   ```
3. **Open the App:** Navigate to `http://127.0.0.1:8000` in your web browser.
4. **Translate:** Click and hold the **"Hold to Speak"** button, say an English sentence, and release to hear the Spanish translation.

## 📁 Project Structure
```text
local-language-translator/
├── templates/
│   └── index.html      # Frontend interface
├── server.py           # Flask server routes
├── worker.py           # AI logic (Whisper, Ollama, TTS)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🔧 Troubleshooting
- **FP16 Warning:** If running on CPU, you may see a warning about FP16. This is handled automatically by the code using `fp16=False`.
- **Empty Transcription:** Ensure your microphone is active and you speak clearly. Whisper requires a second of audio to process effectively.
- **Ollama Connection:** Ensure Ollama is running on `localhost:11434`.

## 📜 License
MIT License. Feel free to use and modify for your own local projects!
