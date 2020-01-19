from live_filter.filters.filter import Filter

import cv2 as cv


class GrayFilter(Filter):
    ''' A filter that turns the image to grayscale. '''

    filter_name = "gray"

    def apply(self, im):
        return cv.cvtColor(im, cv.COLOR_BGR2GRAY)