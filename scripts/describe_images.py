import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize the processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define the input and output directories
input_dir = 'path/to/your/image/dir'
output_dir = 'data/image/whatever'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open the image
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        # Process the image and generate a description
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        description = processor.decode(out[0], skip_special_tokens=True)

        # Save the description to a text file
        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
        with open(output_path, 'w') as f:
            f.write(description)

        print(f"Processed {filename}: {description}")