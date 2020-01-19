from live_filter.filters.filter import Filter

import cv2 as cv


class FlipFilter(Filter):
    ''' Flip the image horizontally. '''
    filter_name = "flip"

    def apply(self, im):
        return cv.flip(im, 1)