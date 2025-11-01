# Put for loop in count

import numpy as np
import cv2 as c
import matplotlib.pyplot as plt

def top_n_colors(i, n):
    # Color detector function
    if i is None:
        return 'No image detected'

    else:
        unqc,C = np.unique(i.reshape(-1, i.shape[-1]), axis=0, return_counts=True)
        topNidx = np.argpartition(C, -n)[-n:]
    return unqc[topNidx], C[topNidx]


image = c.imread('static/test.jpg') #Default is BGR
image = c.cvtColor(image, c.COLOR_BGR2RGB) #Convert to RGB
# print(image.shape)
height, width, channels = image.shape
total_pixels = height * width

colors, top_counts = top_n_colors(i=image, n=30)

colors_flip = np.flipud(colors) #flip RGB values to get most occuring first

top_counts_flip = np.flip(top_counts) #flip total counts to get descending order

colors_flip = colors_flip.tolist()
rgb_values = [tuple(color) for color in colors_flip]
print(rgb_values)

# Do same thing for count values
top_counts_list = top_counts_flip.tolist()
print(top_counts_list)

