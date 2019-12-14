"""
    Main module for Live Filter.
"""

import threading

from control import Control
import imutils
from imutils.video import VideoStream
from flask import Flask, Response, render_template

from args import parse_input
from processing import process_frame, generate


def main():
    """ Main function """
    args = parse_input()
    control = Control()
    control.lock = threading.Lock()
    app = Flask(__name__)
    control.vs = VideoStream(src=0).start()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/video_feed")
    def video_feed():
        # return the response generated along with the specific media
        # type (mime type)
        return Response(generate(control),
                        mimetype="multipart/x-mixed-replace; boundary=frame")

    # start a thread that will perform motion detection
    th = threading.Thread(target=process_frame, args=(control,))
    th.daemon = True
    th.start()

    app.run(host=args.ip, port=args.port, debug=True, threaded=True,
            use_reloader=False)

    # release the video stream pointer
    control.vs.stop()
    
    
if __name__ == "__main__":
    main()
