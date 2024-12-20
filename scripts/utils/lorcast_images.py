import os
import imageio.v3 as iio

# Define the input and output directories
input_dir = 'images/lorcast_api/cards'
output_dir = 'data/images_converted'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate through each image in the input directory and its subdirectories
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith('.avif'):
            # Open the AVIF image
            image_path = os.path.join(root, filename)
            image = iio.imread(image_path)

            # Create the corresponding subdirectory in the output directory
            relative_path = os.path.relpath(root, input_dir)
            output_subdir = os.path.join(output_dir, relative_path)
            os.makedirs(output_subdir, exist_ok=True)

            # Save the image as a JPG file
            output_path = os.path.join(output_subdir, f"{os.path.splitext(filename)[0]}.jpg")
            iio.imwrite(output_path, image, format='jpeg')

print("Conversion complete.")