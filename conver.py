import base64
from PIL import Image
import os
import csv

# Set the input and output folder paths
input_folder = "images"
output_folder = "resized_images"
gray_folder = "resized_gray"


with open('image_info.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Image Name", "Original Size", "Resized Size", "Base64 String Colored", "Base64 String Gray"])

    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Check if file is an image
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
            # Open the image file
            image_path = os.path.join(input_folder, file_name)
            image = Image.open(image_path)

            # Get the original size of the image
            original_size = f"{image.size[0]}x{image.size[1]}"

            # Resize the image to 64x64 pixels without reducing the quality
            # resized_image = image.crop()
            resized_image = image.resize((64, 64))

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, file_name)
            resized_image.save(output_path)
            gray_path = os.path.join(gray_folder, file_name)
            gray_image = resized_image.convert('L')
            gray_image.save(gray_path)


            # Convert the resized image to a base64 string
            with open(output_path, "rb") as image_file:
                base64_string = base64.b64encode(image_file.read()).decode('utf-8')
            with open(gray_path, "rb") as image_file:
                base64_string_gray = base64.b64encode(image_file.read()).decode('utf-8')

            # Get the resized size of the image
            resized_size = f"{resized_image.size[0]}x{resized_image.size[1]}"

            # convet to gray scale


            # Write the image information to the CSV file
            writer.writerow([file_name, original_size, resized_size, base64_string, base64_string_gray])
