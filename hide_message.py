import sys
import numpy as np
import argparse

from PIL import Image
from functools import reduce

class MessageTooLongException(Exception):
    def __init__(self, num_of_bytes, img_size):
        super().__init__("Input message too long fro given image")
        self.num_of_bytes = num_of_bytes
        self.img_size = img_size
        # Oduzima se 1 zbog /0 na kraju
        self.max_text_lenght = int(self.img_size / 8) - 1
        self.message_lenght = int(self.num_of_bytes / 8) - 1

def string_to_ints(chars):
    return [ord(c) for c in chars]

def hide_message(message, img_path):
    message += "\0"
    input_img = Image.open(img_path)

    # Trodimenzionalna matrica: retci * stupci * RGB (3 vrijendosti)
    pixels = np.array(input_img)
    img_shape = pixels.shape

    # Svaki znak u poruci ima 1 bajt. Iz tog razloga zauzima
    # 8 pixela na slici.
    num_of_bytes = len(message) * 8
    img_size = reduce(lambda r, e: r * e, img_shape)
    if num_of_bytes > img_size:
        raise MessageTooLongException(num_of_bytes, img_size)

    # Trodimenzionalna matrica izravnana u jednodimenzionalnu listu
    colors = pixels.flatten()

    chars_as_ints = string_to_ints(message)

    current_index = 0
    for char in chars_as_ints:
        # Prvo se char u binarnom obliku komplementira
        complement = char ^ 0b11111111
        for i in range(8):
            # Zatim se na svakoj boji na slici izvršava XOR
            # operacija sa jednim po jednim bitm od svakog chara.
            # Svakom iteracijom izbacuje se prvi bit jer je on 
            # već dodan na sliku.
            shifted_left = complement << i
            # S obzirom na to da je integer 32-bitan, potrebno je 
            # ostaviti samo zadnjih 8 bitova
            shift_mask = 0b11111111
            shifted_left = shifted_left & shift_mask
            # Konačno prvi bit se stavlja na zadnje mjesto kako
            # bi se mogao napraviti XOR sa svakom bojom slike
            mask = shifted_left >> 7
            # Zadnji bit u 0
            colors[current_index] &= ~0b1
            # XOR zadnjeg bita s maskom
            colors[current_index] ^= mask
            current_index += 1

    # Izravnana jednodimenzionalna lista vraća se u svoj početni
    # oblik trodimenzionalne matrice kako bi se mogla upisati 
    # natrag u sliku
    result_pixels = colors.reshape(img_shape)
    result_image = Image.fromarray(result_pixels)
    result_image.save(img_path)

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Hides given message to an image file.")

    arg_parser.add_argument("message", help="string/file to be hidden in the image")
    arg_parser.add_argument("img_path", help="image where the message will be hidden")
    arg_parser.add_argument("-f", "--file", action="store_true", help="use file instead of string")
    arguments = arg_parser.parse_args()

    message = arguments.message
    img_path = arguments.img_path

    try:
        # Ako je zadana --file opcija, onda se u message
        # ne nalazi sama poruka, već putanja do datoteke
        # u kojoj se nalazi poruka.
        if arguments.file:
            try:
                input_file = open(message)
                message = input_file.read()
                input_file.close
            except FileNotFoundError:
                print("File", message, "does not exist")
                exit()
                
        hide_message(message, img_path)

    except MessageTooLongException as exc:
        print("Message is too long for given image")
        print("Max text length: " + str(exc.max_text_lenght))
        print("Given text length: " + str(exc.message_lenght))
    except FileNotFoundError:
        print("File", img_path, "does not exist")
