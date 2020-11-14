import numpy as np
from PIL import Image

def string_to_ints(chars):
    return [ord(c) for c in chars]

message_to_hide = "KGB"

input_image = Image.open("./examples/example.png")
pixels = np.asarray(input_image)

chars_as_ints = string_to_ints(message_to_hide)
masks = []

print("MESSAGE: ", message_to_hide)
print("MESSAGE AS INTS: ", string_to_ints(message_to_hide))

for index, char in enumerate(chars_as_ints):
    complement = char ^ 0b11111111
    for i in range(8):
        shifted_left = complement << i
        shift_mask = 0b11111111
        shifted_left = shifted_left & shift_mask
        mask = shifted_left >> 7
        masks += [mask]

