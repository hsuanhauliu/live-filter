"""
    Singleton class that holds the shared variables across the system.
"""

from threading import Lock

import cv2 as cv

from filter_manager import FilterManager
from video_stream import StreamManager


class SharedResources:
    """ Class for maintaining shared variables """
    __instance = None


    def __init__(self, vid_src=0):
        if SharedResources.__instance is not None:
            raise Exception("This class is a singleton!")

        SharedResources.__instance = self
        self.output_frame = None
        self.lock = Lock()
        self.vid_stream = StreamManager(src=vid_src)

        # filter variables
        self.filter_m = FilterManager()


    @staticmethod
    def get_instance():
        """ Static access method """
        if SharedResources.__instance is None:
            SharedResources()
        return SharedResources.__instance


    def start_stream(self):
        """ Start video stream """
        self.vid_stream.start()
        
        
    def stop_stream(self):
        """ Stop video stream """
        self.vid_stream.stop()


    def get_filters(self):
        """ Retrieve filters from filter manager """
        return self.filter_m.filters


    def toggle_filter(self, input_filter):
        """ Toggle the selected filter in Filter Manager """
        self.filter_m.toggle_filter(input_filter)
