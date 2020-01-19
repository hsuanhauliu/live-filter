from live_filter.filters.filter import Filter

import cv2 as cv


class BlurFilter(Filter):
    ''' Apply Gaussian blurring to the image. '''

    filter_name = "blurring"

    def apply(self, im):
        im = cv.blur(im, (5, 5))
        return im