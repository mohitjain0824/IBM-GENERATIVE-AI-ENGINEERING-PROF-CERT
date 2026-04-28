from flask import Flask, render_template, request, jsonify
import os
from worker import init_llm, process_document, process_prompt

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize the models on startup
init_llm()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-pdf', methods=['POST'])
def process_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    # Logic from worker.py
    process_document(file_path)
    
    return jsonify({"status": "Successfully processed " + file.filename})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    # Get answer from local Ollama via worker.py
    response = process_prompt(user_message)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(port=8000, debug=True)