# Simple Chatbot with Hugging Face

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A minimal terminal-based chatbot powered by Hugging Face's BlenderBot model. This project demonstrates how to build a conversational AI using open-source transformers.

## Features

- Interactive terminal chatbot
- Conversation history tracking
- Uses pre-trained BlenderBot model for responses
- Easy setup with virtual environment

## Prerequisites

- Python 3.8 or higher
- Internet connection for initial model download

## Installation

1. Clone or download this repository.

2. Navigate to the project folder:
   ```bash
   cd createChatGPTLikeWebsite
   ```

3. Create and activate a virtual environment:
   ```powershell
   python -m venv my_env
   .\my_env\Scripts\Activate.ps1
   ```

4. Upgrade pip:
   ```powershell
   python -m pip install --upgrade pip
   ```

5. Install dependencies:
   ```powershell
   python -m pip install transformers torch
   ```
   > **Note:** If using Python 3.12, you may need to specify `transformers==5.6.2` for compatibility.

## Usage

Run the chatbot:
```powershell
python chatbot.py
```

- Type your message at the prompt (`> `) and press Enter.
- The chatbot will respond based on the conversation history.
- Exit by pressing `Ctrl+C`.

Example interaction:
```
> Hello, how are you?
I'm doing well, thank you! How about you?
```

## Project Structure

```
createChatGPTLikeWebsite/
├── chatbot.py          # Main chatbot script
├── my_env/             # Virtual environment (created during setup)
├── README.md           # This file
└── __pycache__/        # Python cache files
```

## How It Works

1. **Model Loading:** Downloads and loads the BlenderBot model from Hugging Face.
2. **Tokenization:** Converts user input into tokens for the model.
3. **Generation:** Uses the transformer model to generate responses.
4. **History Tracking:** Maintains conversation context for coherent replies.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Based on IBM's Generative AI Engineering Professional Certificate course material.
- Uses Hugging Face Transformers library.
- BlenderBot model by Facebook AI Research.

## Author

Created as part of the IBM Generative AI Engineering Professional Certificate.
