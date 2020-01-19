from live_filter.filters.filter import Filter

import cv2 as cv
import numpy as np


class WindowFilter(Filter):
    ''' Create a window effect using 4 smaller versions of the image.'''

    filter_name = "window"

    def apply(self, im):
        new_size = (im.shape[1] // 2, im.shape[0] // 2)
        new_im = cv.resize(im, new_size)
        res = np.concatenate((new_im, new_im), axis=1)
        return np.concatenate((res, res), axis=0)
