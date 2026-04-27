# Simple Chatbot with Hugging Face

A minimal terminal chatbot using a Hugging Face BlenderBot model.

## Setup

1. Open PowerShell in this folder.
2. Activate the virtual environment:
   ```powershell
   .\my_env\Scripts\Activate.ps1
   ```
3. Upgrade pip:
   ```powershell
   python -m pip install --upgrade pip
   ```
4. Install dependencies:
   ```powershell
   python -m pip install transformers torch
   ```

## Run

```powershell
python chatbot.py
```

Type a message at the prompt and press Enter. Exit with `Ctrl+C`.

## Notes

- First run downloads the model from Hugging Face.
- If `transformers` install fails for Python 3.12, use `transformers==5.6.2`.
- The script stores conversation history in memory only for the current session.
