from faster_whisper import WhisperModel
import os

def transcribe_audio(file_path):
    # We use the 'base' model for speed. 
    # Use 'small' or 'medium' if you want higher accuracy.
    # device="cpu" ensures it runs on your processor. 
    # compute_type="int8" makes it fast and light on RAM.
    model_size = "base"
    
    print(f"--- Loading Local Whisper Model ({model_size})... ---")
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    print(f"--- Transcribing: {file_path} ---")
    # beam_size=5 is a standard for balancing speed and quality
    segments, info = model.transcribe(file_path, beam_size=5)

    print(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")

    full_text = ""
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        full_text += segment.text + " "

    return full_text.strip()

if __name__ == "__main__":
    # Change 'sample_audio.mp3' to the name of a file in your audio_files folder
    test_file = "./audio_files/test_audio_file.mp3" 
    
    if os.path.exists(test_file):
        result = transcribe_audio(test_file)
        print("\n--- FINAL TRANSCRIPTION ---")
        print(result)
    else:
        print(f"Error: Could not find {test_file}. Please add an audio file to the folder.")