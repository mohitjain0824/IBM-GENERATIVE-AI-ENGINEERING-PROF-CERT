# Local AI Meeting Companion 🎙️

A 100% local, private, and free AI-powered meeting assistant. This project transcribes audio recordings using **OpenAI's Whisper** (via `faster-whisper`) and generates professional summaries using **Llama 3** (via **Ollama**). 

No data leaves your machine. No API keys required. No costs.

## ✨ Features
- **Local Transcription:** Uses `faster-whisper` with `int8` quantization for high-speed, CPU-efficient speech-to-text.
- **Local LLM Summarization:** Integrates with `Ollama` to run `Llama 3` for generating meeting minutes, key decisions, and action items.
- **Privacy First:** Designed for sensitive business meetings where data privacy is paramount.
- **User-Friendly UI:** Built with `Gradio` for a simple, browser-based drag-and-drop experience.

## 🛠️ Tech Stack
- **STT Engine:** [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- **LLM Runtime:** [Ollama](https://ollama.com/)
- **Orchestration:** Python, LangChain
- **UI:** [Gradio](https://www.gradio.app/)
- **Processing:** [FFmpeg](https://ffmpeg.org/)

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **FFmpeg:** Must be installed and added to your system PATH.
- **Ollama:** Download and install from [ollama.com](https://ollama.com/).

### 2. Setup Ollama
After installing Ollama, pull the Llama 3 model:
```bash
ollama pull llama3
```

### 3. Installation
Clone this repository and set up the virtual environment:
```bash
# Create a project folder
mkdir local-ai-meeting-companion
cd local-ai-meeting-companion

# Create a virtual environment
python -m venv ai_meeting_env
source ai_meeting_env/bin/activate  # On Windows use: ai_meeting_env\\Scripts\\activate

# Install dependencies
pip install faster-whisper ollama gradio langchain-community
```

### 4. Project Structure
```text
.
├── app.py           # Main Gradio application (UI)
├── stt_engine.py    # Whisper transcription logic
├── llm_engine.py    # Ollama/Llama 3 summarization logic
├── audio_files/     # Directory for storing audio samples
└── README.md
```

### 5. Running the App
1. Ensure the Ollama service is running in the background.
2. Activate your virtual environment.
3. Run the application:
```bash
python app.py
```
4. Open your browser and navigate to `http://127.0.0.1:7860`.

## ⚙️ How it Works
1. **Audio Decoding:** `FFmpeg` decodes the uploaded audio into a format the Whisper model can process.
2. **Transcription:** `faster-whisper` performs inference locally on your CPU/GPU to generate text.
3. **Summarization:** The generated text is passed to the local `Ollama` instance where `Llama 3` extracts key points and action items based on a specialized system prompt.

## 📜 License
This project is for educational purposes and is inspired by the IBM Generative AI Engineering Professional Certificate.