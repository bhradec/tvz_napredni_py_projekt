import sys
import numpy as np

from PIL import Image

input_img_path = sys.argv[1]
input_img = Image.open(input_img_path)
pixels = np.array(input_img)
print(pixels)