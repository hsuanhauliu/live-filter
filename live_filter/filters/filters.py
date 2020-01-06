"""
    Various image filters.
"""

import cv2 as cv
import numpy as np


class GrayFilter:
    name = "gray"

    def __init__(self):
        pass


    def apply(self, im):
        return cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        
        
class BlurFilter:
    name = "blurring"

    def __init__(self):
        pass


    def apply(self, im):
        im = cv.blur(im, (5, 5))
        return im


class FlipFilter:
    name = "flip"
    
    def __init__(self):
        pass
        
        
    def apply(self, im):
        return cv.flip(im, 1)
        

class WindowFilter:
    """
        Create a window effect using 4 smaller versions of the image.
    """
    name = "window"
    
    def __init__(self):
        pass
        
    
    def apply(self, im):
        new_size = (im.shape[1] // 2, im.shape[0] // 2)
        new_im = cv.resize(im, new_size)
        res = np.concatenate((new_im, new_im), axis=1)
        return np.concatenate((res, res), axis=0)