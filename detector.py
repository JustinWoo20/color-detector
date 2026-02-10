import cv2
import numpy as np
import matplotlib as plt
import rgb2hex

class ColorDetector:
    def __init__(self, image, n):
        self.image = image
        self.n = n
        self.rgb_colors, self.count = self.top_n_colors(i=self.image, n=self.n)
        self.hex_colors = self.convert_to_hex(colors=self.rgb_colors)
        self.color_dict = self.color_frequency(i=self.image, counts=self.count, hex_c=self.hex_colors)

    def top_n_colors(self, i, n):
        # Color detector function
        if i is None:
            return 'No image detected'
        else:
            # Find unique colors
            unqcolor, C = np.unique(i.reshape(-1, i.shape[-1]), axis=0, return_counts=True)
            # Find top n colors
            topNidx = np.argpartition(C, -n)[-n:]
            # Sort in descending order
            topN_sorted = topNidx[np.argsort(C[topNidx])[::-1]]

            return unqcolor[topN_sorted], C[topN_sorted]

    def convert_to_hex(self, colors):
        # convert rgb values to color hexcodes
        color_list = colors.tolist()
        hex_colors = [rgb2hex.rgb2hex(rgb) for rgb in color_list]
        return hex_colors

    def color_frequency(self, i, counts, hex_c):
        total_pixels = i.shape[0] * i.shape[1]
        frequency = [c / total_pixels for c in counts]
        color_freq = dict(zip(hex_c, frequency))
        color_freq = {color: float(freq) for color, freq in color_freq.items()}
        return color_freq

test = ColorDetector(image=cv2.imread('static/img/colors_test.png', cv2.IMREAD_COLOR_RGB), n=5)


