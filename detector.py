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
print(image.shape)
height, width, channels = image.shape
total_pixels = height * width

colors, top_counts = top_n_colors(i=image, n=30)

colors_flip = np.flipud(colors)
# print(colors_flip)

top_counts_flip = np.flip(top_counts)
print(top_counts_flip)

for count in top_counts_flip:
    pct_of_img = round((count / total_pixels), 4) * 100
    print(pct_of_img)
