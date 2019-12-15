"""
    Singleton class that holds the shared variables across the system.
"""

from threading import Lock

from imutils.video import VideoStream


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
        self.filters = []   # filters


    @staticmethod
    def get_instance():
        """ Static access method """
        if SharedResources.__instance is None:
            SharedResources()
        return SharedResources.__instance


    def start_stream(self):
        """ Start video stream """
        self.vid_stream.start()
