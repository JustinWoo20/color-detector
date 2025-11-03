import cv2
import numpy as np
import matplotlib as plt
import rgb2hex

class ColorDetector:
    def __init__(self, image, n):
        self.image = image
        self.n = n
        self.colors, self.count = self.top_n_colors(i=self.image, n=self.n)
        self.color_data = self.sort_colors(i=self.image, colors=self.colors, count=self.count)

    def top_n_colors(self, i, n):
        # Color detector function
        if i is None:
            return 'No image detected'
        else:
            unqcolor, C = np.unique(i.reshape(-1, i.shape[-1]), axis=0, return_counts=True)
            topNidx = np.argpartition(C, -n)[-n:]
            return unqcolor[topNidx], C[topNidx]

    def sort_colors(self, i, colors, count):
        height, width, channels = i.shape
        total_pixels = height * width
        # Flip for descending order
        colors_flip = np.flipud(colors)
        top_counts_flip = np.flip(count)

        #Convert to lists
        colors_flip = colors_flip.tolist()
        hex_code = [rgb2hex.rgb2hex(rgb) for rgb in colors_flip]
        top_counts_list = top_counts_flip.tolist()
        pct_of_img = [round(((number / total_pixels) * 100), 4) for number in top_counts_list]

        #Put everything together into 1 dictionary
        color_data = [
            {'hex': hex_code[i], 'percentage': pct_of_img[i]}
            for i in range(len(hex_code))
        ]
        return color_data

test = ColorDetector(image=cv2.imread('static/test_2.jpg'), n=10)
print(test.color_data)


