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
colors, top_counts = top_n_colors(i=image, n=10)

print(colors)
print(top_counts)

