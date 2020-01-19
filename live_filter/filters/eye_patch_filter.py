from live_filter.filters.filter import Filter

import cv2 as cv
import dlib


class EyePatchFilter(Filter):
    ''' Superimpose an eye patch on the face. '''

    filter_name = "eye patch"


    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(
            'live_filter/filters/models/dlib/shape_predictor_68_face_landmarks.dat')


    def apply(self, im):
        gray_frame = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        faces = self.detector(gray_frame)

        for face in faces:
            landmarks = self.predictor(gray_frame, face)
            right_eye_x = (landmarks.part(43).x + landmarks.part(46).x) // 2
            right_eye_y = (landmarks.part(43).y + landmarks.part(46).y) // 2
            right_eye_r = int((((landmarks.part(45).x - landmarks.part(42).x) ** 2 +
                                (landmarks.part(45).y - landmarks.part(42).y) ** 2) **
                                (1/2)) / 2)

            # draw one the image
            cv.circle(im, (right_eye_x, right_eye_y), right_eye_r, (0, 0, 0), -1)
            cv.line(im, (landmarks.part(19).x, landmarks.part(19).y),
                    (landmarks.part(44).x, landmarks.part(44).y), (0, 0, 0), 4)
            cv.line(im, (landmarks.part(47).x, landmarks.part(47).y),
                    (landmarks.part(15).x, landmarks.part(15).y), (0, 0, 0), 4)

        return im
