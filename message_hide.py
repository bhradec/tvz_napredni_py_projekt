import sys
import numpy as np

from PIL import Image

def string_to_ints(chars):
    return [ord(c) for c in chars]

message_to_hide = sys.argv[1]
input_img_path = sys.argv[2]

input_img = Image.open(input_img_path)

# Trodimenzionalna matrica: retci * stupci * RGB (3 vrijendosti)
pixels = np.array(input_img)
img_shape = pixels.shape

# Trodimenzionalna matrica izravnana u jednodimenzionalnu listu
colors = pixels.flatten()

chars_as_ints = string_to_ints(message_to_hide)

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
        colors[current_index] ^= mask
        current_index += 1

# Izravnana jednodimenzionalna lista vraća se u svoj početni
# oblik trodimenzionalne matrice kako bi se mogla upisati 
# natrag u sliku
result_pixels = colors.reshape(img_shape)
result_image = Image.fromarray(result_pixels)
result_image.save(input_img_path)
