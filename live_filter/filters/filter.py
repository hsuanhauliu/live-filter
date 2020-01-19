"""
    Abstract base Filter class.
"""

from abc import ABC, abstractmethod


class Filter(ABC):
    ''' Abstract base class for other filters.

    Each new filter subclass needs to inherit from this base class to ensure
    that the abstract method(s) to be implemented.
    '''

    filter_name = None

    @abstractmethod
    def apply(self, im):
        ''' Apply the filter to the input image. '''
        pass


    @property
    def name(self):
        ''' Get the name of the filter class. '''
        if self.filter_name is None:
            raise ValueError('Filter name has not been specified.')
        return self.filter_name
