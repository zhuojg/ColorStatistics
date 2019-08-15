import matplotlib.pyplot as plt
import cv2
import numpy as np


class ColorStatistics:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)

    def gray_statistics(self, bins):
        im_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        plt.hist(im_gray.ravel(), bins=bins, range=[0, 256])
        plt.show()

    def color_statistics(self, bins):
        fig, ax = plt.subplots()
        bgr_color = ['b', 'g', 'r']
        line = []

        for cidx, color in enumerate(bgr_color):
            hist = cv2.calcHist([self.img], [cidx], None, [bins], [0, 256])
            line_temp, = ax.plot(hist, color=color, label=color)
            line.append(line_temp)

        plt.legend(handles=line, labels=['Blue', 'Green', 'Red'], loc='best')
        plt.show()


if __name__ == '__main__':
    cs = ColorStatistics('timg-3.jpg')
    cs.color_statistics(bins=256)
