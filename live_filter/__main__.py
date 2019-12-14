"""
    Main module for Live Filter.
"""


import argparse
import threading
import time

import cv2
import imutils
from imutils.video import VideoStream
from flask import Flask, Response, render_template


def main():
    """ Main function """
    args = parse_input()

    global output_frame, lock, vs
    output_frame = None
    lock = threading.Lock()
    app = Flask(__name__)   # initialize a flask object

    vs = VideoStream(src=0).start()


    @app.route("/")
    def index():
        """"""
        return render_template("index.html")


    @app.route("/video_feed")
    def video_feed():
        """"""
        # return the response generated along with the specific media
        # type (mime type)
        return Response(generate(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")


    # start a thread that will perform motion detection
    th = threading.Thread(target=process_frame)
    th.daemon = True
    th.start()

    app.run(host=args.ip, port=args.port, debug=True, threaded=True,
            use_reloader=False)

    # release the video stream pointer
    vs.stop()



def parse_input():
    """ Argument parsing function """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, default="0.0.0.0",
                        help="ip address of the device")
    parser.add_argument("-o", "--port", type=int, default=8000,
                        help="ephemeral port number of the server (1024 to 65535)")
    return parser.parse_args()



def process_frame():
    """ Process frame """
    global output_frame, vs, lock

    # loop over frames from the video stream
    while True:
        # read the next frame from the video stream, resize it,
        # convert the frame to grayscale, and blur it
        frame = vs.read()
        frame = imutils.resize(frame, width=800)

        #TODO do processing here

        # acquire the lock, set the output frame, and release the lock
        with lock:
            output_frame = frame.copy()


def generate():
    """ Generate frame """
    global lock, output_frame

    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if output_frame is None:
                continue

            # encode the frame in JPEG format
            flag, encoded_img = cv2.imencode(".jpg", output_frame)

            if not flag:
                continue

        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(encoded_img) + b'\r\n')


if __name__ == "__main__":
    main()
