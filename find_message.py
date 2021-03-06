import sys
import numpy as np
import argparse

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

            if character_byte == ord("\0"):
                break

            message += chr(character_byte)
            character_byte = 0x00

        # Uzima zadnji bit iz boje te ga invertira.
        last_byte = color & 0b00000001
        last_byte = ~last_byte
        last_byte = last_byte & 0b00000001

        # Upisuje zadnji bit iz boje na zadnje mjesto charactera.
        character_byte = character_byte | last_byte

        # Sve bitove pomice za jedno mjesto u lijevo
        # time dodaje nulu na desnoj strani
        # to radi kako bi u sljedecem loopu
        # na mjesto nule upisao last_byte.
        character_byte = character_byte << 1

    return message

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Finds a hidden message from an image file.")

    arg_parser.add_argument("img_path", help="image where the message is hidden")
    arg_parser.add_argument("-o", "--output", help="file to write message in")
    arguments = arg_parser.parse_args()

    img_path = arguments.img_path
    out_path = arguments.output

    try:
        message = find_message(img_path)
        if arguments.output:  
            output_file = open(arguments.output, "w")
            output_file.write(message)
            output_file.close()
        else:
            print(message)
    except FileNotFoundError:
        print("File", img_path, "does not exist")
