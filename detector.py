import numpy as np

class ColorDetector:
    def __init__(self, image, n):
        self.image = image
        self.n = n
        self.colors, self.count = self.top_n_colors(i=self.image, n=self.n)
        self.rgb, self.pct = self.sort_colors(i=self.image, colors=self.colors, count=self.count)

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

        colors_flip = np.flipud(colors)  # flip RGB values to get most occuring first
        top_counts_flip = np.flip(count)  # flip total counts to get descending order

        colors_flip = colors_flip.tolist()
        rgb_values = [tuple(color) for color in colors_flip] #Create tuple list of RGB values

        # Do same thing for count values
        top_counts_list = top_counts_flip.tolist()
        pct_of_img = [round(((number / total_pixels) * 100), 4) for number in top_counts_list]
        return rgb_values, pct_of_img


