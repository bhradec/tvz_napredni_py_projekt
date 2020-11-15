import sys
import numpy as np

from PIL import Image

def display_pixels(img_path):
    input_img = Image.open(img_path)
    pixels = np.array(input_img)
    print(pixels)

if __name__ == "__main__":
    img_path = sys.argv[1]

    if img_path:
        display_pixels(img_path)
    else:
        print("No image path given")
        print("Help: display_pixels.py img_path")
