from typing import Iterable


class IntegerList(list):
    '''The IntegerList should only accept integers
    '''
    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError("Not an integer type")
        
    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def __add__(self, __iterable):
        for element in __iterable:
          IntegerList.check_value_type(element)
          
        list.__add__(self, __iterable)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, __iterable: Iterable):
        for element in __iterable:
            IntegerList.check_value_type(element)

        list.extend(self, __iterable)

    def insert(self, index, value):
        IntegerList.check_value_type(value)
        list.insert(self, index, value)

    