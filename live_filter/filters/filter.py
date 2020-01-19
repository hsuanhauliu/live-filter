"""
    Abstract base Filter class.
"""

from abc import ABC, abstractmethod


class Filter(ABC):
    ''' Abstract base class for other filters.

    Each new filter subclass needs to inherit from this base class to ensure
    that the abstract method(s) to be implemented.
    '''

    filter_name = "base_filter"

    @abstractmethod
    def apply(self, im):
        ''' Apply the filter to the input image. '''
        pass


    @property
    def name(self):
        ''' Get the name of the filter class. '''
        return self.filter_name
