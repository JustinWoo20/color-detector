import numpy as np
import cv2 as c

def top_colors(i, n):
    unqc,C = np.unique(i.reshape(-1, i.shape[-1]), axis=0, return_counts=True)
    topNidx = np.argpartition(C, -n)[-n:]
    return unqc[topNidx], C[topNidx]


image = c.imread('static/test.jpg')
print(top_colors(i=image, n=10))

