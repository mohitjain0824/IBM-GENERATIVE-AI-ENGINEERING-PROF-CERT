# Image Captioning Lab (BLIP)

This lab contains three working scripts using `Salesforce/blip-image-captioning-base`.

## What this code does

### 1) `image_cap.py`

- Captions one local image (`image.png`)
- Prints caption in terminal

### 2) `image_captioning_app.py`

- Runs a Gradio web app
- Accepts uploaded image
- Returns generated caption

### 3) `automate_url_captioner.py`

- Fetches images from a webpage
- Generates captions for valid images
- Writes results to `captions.txt`

## Files

- `image_cap.py` - main script
- `image_captioning_app.py` - Gradio UI app
- `automate_url_captioner.py` - caption images from URL
- `image.png` - sample image
- `captions.txt` - generated captions output file
- `requirements.txt` - Python dependencies

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python image_cap.py
```

```bash
python image_captioning_app.py
```

```bash
python automate_url_captioner.py
```
