# import cv2
import numpy as np
import matplotlib as plt
import rgb2hex

class ColorDetector:
    def __init__(self, image, n):
        self.image = image
        self.n = n
        self.rgb_colors, self.count = self.top_n_colors(i=self.image, n=self.n)
        self.hex_colors = self.convert_to_hex(colors=self.rgb_colors)
       # self.color_data = self.sort_colors(i=self.image, colors=self.colors, count=self.count)

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
        print(color_list)
        hex_colors = [rgb2hex.rgb2hex(rgb) for rgb in color_list]
        return hex_colors

test = ColorDetector(image=cv2.imread('static/img/colors_test.png', cv2.IMREAD_COLOR_RGB), n=5)
print(test.hex_colors)


