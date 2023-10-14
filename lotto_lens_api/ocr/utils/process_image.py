from PIL import Image, ImageFilter
import numpy as np
import io


def process_image(file):
    # Load the image
    image = Image.open(file)
    file_name = "processed_file.jpg"

    # Convert to grayscale (if it's a color image)
    gray_image = image.convert('L')
    sharpened_image = gray_image.filter(
        ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    sharpened_image.save(file_name, format="JPEG")

    return file_name
