import sys
import numpy as np

from PIL import Image

def find_message(img_path):
    input_img = Image.open(img_path)
    pixels = np.array(input_img)

    colors = pixels.flatten()

    message = ""
    character_byte = 0x00

    for i, color in enumerate(colors):
        if i % 8 == 0 and i != 0:
            character_byte = character_byte >> 1
            message += chr(character_byte)
            character_byte = 0x00

        # Uzima zadnji bit iz boje te ga invertira
        last_byte = color & 0b00000001
        last_byte = ~last_byte
        last_byte = last_byte & 0b00000001

        # Upisuje zadnji bit iz boje na zadnje mjesto charactera
        character_byte = character_byte | last_byte

        # Sve bitove pomice za jedno mjesto u lijevo
        #  time dodaje nulu na desnoj strani
        #  to radi kako bi u sljedecem loopu
        #  na mjesto nule upisao last_byte
        character_byte = character_byte << 1

    print("The hiden message:")
    print(message)

if __name__ == "__main__":
    img_path = sys.argv[1]

    if img_path:
        find_message(img_path)
    else:
        print("No image path given")
        print("Help: message_find.py img_path")