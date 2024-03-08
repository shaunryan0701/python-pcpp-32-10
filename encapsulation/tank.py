class TankException(Exception):
    pass

class Tank:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__level = 0

    @property
    def level(self):
        return self.__level
    
    @property
    def capacity(self):
        return self.__capacity

    @level.setter
    def level(self, level):
        if level >0:
            if level <= self.__capacity:
                self.__level = level
            else:
                raise TankException('Too much liquid in the tank')
        elif level < 0:
            raise TankException('Not possible to set negative level')

    @level.deleter
    def level(self):
        if self.__level > 0:
            print('Warning: Liquid in the tank will be lost')
            del self.__level
        else:
            print('The tank is already empty')