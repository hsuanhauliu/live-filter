"""
    Filter manager.
"""

from live_filter.filters.filters import *


class FilterManager:
    """ Manager class for the filters """
    #TODO list values as functions for selecting each filter
    filter_dict = {
        "blurring": BlurFilter(),
        "gray": GrayFilter(),
    }


    def __init__(self):
        self.filter_set = set() # set of filter strings
        self.filter_list = []   # ordered filter objects


    @property
    def filters(self):
        """ List of Filter Objects """
        return self.filter_list
        
        
    def toggle_filter(self, input_filter):
        if input_filter in self.filter_set:
            self._remove_filter(input_filter)
        else:
            self._add_filter(input_filter)


    def _add_filter(self, input_filter):
        """ Add selected filter """
        self.filter_set.add(input_filter)
        self.filter_list.append(self.filter_dict[input_filter])


    def _remove_filter(self, input_filter):
        """ Remove target filter """
        self.filter_set.remove(input_filter)
        self.filter_list.remove(self.filter_dict[input_filter])
        