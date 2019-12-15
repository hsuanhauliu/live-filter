"""
    Frame processing module.
"""

import cv2 as cv
import imutils
from shared_resources import SharedResources


def process_frame():
    """ Process frame """
    resources = SharedResources.get_instance()

    # loop over frames from the video stream
    while True:
        frame = resources.vid_stream.read()
        frame = imutils.resize(frame, width=800)

        for fil in resources.filters:
            frame = fil.apply(frame)

        # acquire the lock, set the output frame, and release the lock
        with resources.lock:
            resources.output_frame = frame.copy()


def encode():
    """ Encode frame to render """
    resources = SharedResources.get_instance()

    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with resources.lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if resources.output_frame is None:
                continue

            # encode the frame in JPEG format
            flag, encoded_img = cv.imencode(".jpg", resources.output_frame)

            if not flag:
                continue

        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(encoded_img) + b'\r\n')
