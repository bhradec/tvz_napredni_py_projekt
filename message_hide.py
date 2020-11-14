import sys
import numpy as np

from PIL import Image

def string_to_ints(chars):
    return [ord(c) for c in chars]

message_to_hide = sys.argv[1]
input_img_path = sys.argv[2]
input_img = Image.open(input_img_path)

pixels = np.array(input_img)
img_shape = pixels.shape

colors = np.copy(pixels)
colors = colors.flatten()

chars_as_ints = string_to_ints(message_to_hide)

current_index = 0
for index, char in enumerate(chars_as_ints):
    complement = char ^ 0b11111111
    for i in range(8):
        shifted_left = complement << i
        shift_mask = 0b11111111
        shifted_left = shifted_left & shift_mask
        mask = shifted_left >> 7
        colors[current_index] ^= mask
        current_index += 1

result_pixels = colors.reshape(img_shape)
result_image = Image.fromarray(result_pixels)

result_image.save(input_img_path)
