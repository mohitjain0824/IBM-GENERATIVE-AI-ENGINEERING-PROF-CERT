import gradio as gr
from stt_engine import transcribe_audio
from llm_engine import summarize_text
import os

def process_meeting(audio_file):
    if audio_file is None:
        return "Error: No audio file uploaded.", "No transcription available."

    try:
        # 1. Transcribe the uploaded audio locally
        print(f"Starting local transcription for: {audio_file}")
        transcription = transcribe_audio(audio_file)
        
        # 2. Summarize the text using Ollama
        print("Starting local summarization...")
        summary = summarize_text(transcription)
        
        return transcription, summary
    except Exception as e:
        return f"An error occurred: {str(e)}", "Error generating summary."

# Define the Gradio Interface
with gr.Blocks(title="Local AI Meeting Companion") as demo:
    gr.Markdown("# 🎙️ Local AI Meeting Companion")
    gr.Markdown("Upload a meeting recording to get a transcription and a summary—100% local and private.")
    
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload Meeting Audio")
    
    with gr.Row():
        process_btn = gr.Button("Process Meeting", variant="primary")
        
    with gr.Column():
        transcription_output = gr.Textbox(label="Full Transcription", lines=10)
        summary_output = gr.Markdown(label="AI Summary")

    # Connect the button to our function
    # Adding 'show_progress=True' gives the user a loading spinner
    process_btn.click(
        fn=process_meeting,
        inputs=audio_input,
        outputs=[transcription_output, summary_output],
        show_progress="full" 
    )

if __name__ == "__main__":
    # Launch the local web server
    demo.launch(server_name="127.0.0.1", server_port=7860)