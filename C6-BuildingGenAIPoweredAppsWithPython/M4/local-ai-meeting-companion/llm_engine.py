import ollama

def summarize_text(transcription):
    if not transcription or len(transcription.strip()) < 5:
        return "The transcription was too short to summarize."

    print("--- Sending to local Llama 3 (Ollama)... ---")
    
    system_prompt = (
        "You are a professional business assistant. Summarize the following meeting transcription. "
        "Highlight the key decisions and next steps using bullet points."
    )
    
    try:
        # We explicitly use 'llama3' (ensure this matches 'ollama list')
        response = ollama.chat(
            model='llama3',
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': transcription},
            ],
        )
        return response['message']['content']
    except Exception as e:
        return f"Ollama Error: {str(e)}"