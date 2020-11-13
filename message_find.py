import tkinter as tk
import cv2

img = cv2.imread("./input.png")
rows, cols = img.shape

for row in range(rows):
    for col in range(cols):
        pixel = img[row][col]
        print(pixel)

