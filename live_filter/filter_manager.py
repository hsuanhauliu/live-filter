from filters import *


class FilterManager:
    """ Manager class for the filters """
    #TODO list values as functions for selecting each filter
    filter_dict = {
        "blurring": 1,
        "gray": 2
    }


    def __init__(self):
        self.filters = set()


    def add_filter(self, input_filter):
        """ Add selected filter """
        print("add selected filter:", input_filter)
        print("id:", self.filter_dict[input_filter])


    def remove_filter(self, input_filter):
        """ Remove target filter """
        print("delete selected filter:", input_filter)
        print("id:", self.filter_dict[input_filter])
