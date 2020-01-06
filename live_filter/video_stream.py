"""
    Manager class for handling video stream. Modified code of the imutils
    package, WebcamVideoStream class:
    https://github.com/jrosebr1/imutils/blob/master/imutils/video/webcamvideostream.py
"""

from threading import Thread

import cv2 as cv


class StreamManager:
    def __init__(self, src=0):
        self.name = "VideoStreamManager"
        self.stopped = False
        
        self.stream = cv.VideoCapture(src)
        _, self.frame = self.stream.read()
        
        
    def start(self):
        """ Start video stream thread """
        th = Thread(target=self.update, name=self.name, daemon=True)
        th.start()
        return self
        
        
    def update(self):
        """ Keep updating current frame """
        while True:
            _, self.frame = self.stream.read()
            if self.stopped:
                return
            

    def read(self):
        """ Return the newest frame """
        return self.frame
        
    
    def stop(self):
        """ Stop the video stream """
        self.stopped = True