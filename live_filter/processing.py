"""
    Frame processing module.
"""

import cv2 as cv
import imutils


def process_frame(control):
    """ Process frame """
    # loop over frames from the video stream
    while True:
        frame = control.vs.read()
        frame = imutils.resize(frame, width=800)

        for fil in control.filters:
            frame = fil.apply(frame)

        # acquire the lock, set the output frame, and release the lock
        with control.lock:
            control.output_frame = frame.copy()


def generate(control):
    """ Generate frame to render """
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with control.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if control.output_frame is None:
                continue

            # encode the frame in JPEG format
            flag, encoded_img = cv.imencode(".jpg", control.output_frame)

            if not flag:
                continue

        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(encoded_img) + b'\r\n')
