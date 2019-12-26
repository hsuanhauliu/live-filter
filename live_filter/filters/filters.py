"""
    Various image filters.
"""

import cv2 as cv


class GrayFilter:
    name = "gray"

    def __init__(self):
        pass


    def apply(self, im):
        return im
        
        
class BlurFilter:
    name = "blurring"

    def __init__(self):
        pass


    def apply(self, im):
        im = cv.blur(im, (5, 5))
        return im
