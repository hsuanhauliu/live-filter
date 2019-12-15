"""
    Main module for Live Filter.
"""

import threading

from shared_resources import SharedResources
from flask import Flask, Response, render_template

from args import parse_input
from processing import process_frame, encode


def main():
    """ Main function """
    args = parse_input()
    app = Flask(__name__)

    # initialize resources singleton class
    shared = SharedResources(vid_src=0)
    shared.start_stream()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/video_feed")
    def video_feed():
        # return the response generated along with the specific media
        # type (mime type)
        return Response(encode(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")

    # start a thread that will perform filtering
    processing_th = threading.Thread(target=process_frame, daemon=True)
    processing_th.start()

    app.run(host=args.ip, port=args.port, debug=True, threaded=True,
            use_reloader=False)

    shared.vid_stream.stop()


if __name__ == "__main__":
    main()
