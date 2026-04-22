from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_path = r"C:\Mj\Coursera\ibmgaepc\C6\M1\image.png"
image = Image.open(img_path).convert('RGB')

inputs = processor(images=image, text="the image of", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print(caption)