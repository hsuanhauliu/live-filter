"""
    Singleton class that holds the shared variables across the system.
"""

from threading import Lock

from imutils.video import VideoStream

from filter_manager import FilterManager


class SharedResources:
    """ Class for maintaining shared variables """
    __instance = None


    def __init__(self, vid_src=0):
        if SharedResources.__instance is not None:
            raise Exception("This class is a singleton!")

        SharedResources.__instance = self
        self.output_frame = None
        self.lock = Lock()
        self.vid_stream = VideoStream(src=vid_src)

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


    def add_filter(self, input_filter):
        """ Add selected filter to the filter manager """
        self.filter_m.add_filter(input_filter)


    def remove_filter(self, input_filter):
        """ Remove selected filter from the filter manager """
        self.filter_m.remove_filter(input_filter)
