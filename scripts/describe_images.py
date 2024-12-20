import os
import json
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import pillow_avif

# Initialize the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define the input and output directories
input_dir = 'images/lorcast_api/cards'
output_dir = 'data/images'

# Initialize an empty dictionary to store descriptions
descriptions = {}

os.makedirs(output_dir, exist_ok=True)

# Iterate through each image in the input directory and its subdirectories
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.avif')):
            # Open the image
            image_path = os.path.join(root, filename)
            image = Image.open(image_path)

            # Process the image and generate a description
            inputs = processor(images=image, return_tensors="pt")
            out = model.generate(**inputs)
            description = processor.decode(out[0], skip_special_tokens=True)

            # Store the description in the dictionary
            relative_path = os.path.relpath(root, input_dir)
            image_key = os.path.join(relative_path, filename)
            descriptions[image_key] = description

            print(f"Processed {filename}: {description}")

# Write all descriptions to a single JSON file
output_json_path = os.path.join(output_dir, "descriptions.json")
with open(output_json_path, 'w') as json_file:
    json.dump(descriptions, json_file, indent=4)