class Tyre:
    def __init__(self, size) -> None:
        self.__pressure = 30
        self.__size = size

    @property
    def pressure(self):
        return self.__pressure
    
    @pressure.setter
    def pressure(self, new_pressure):
        if new_pressure > 30:
            print(f'Pressure to high')
            self.__pressure = 30
        else: 
            self.__pressure = new_pressure

    @property
    def size(self):
        return self.__size
    
    def pump(self):
        print(f'I am pumping the tyre')