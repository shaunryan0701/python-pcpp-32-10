class Engine:
    def __init__(self, fuel_type) -> None:
        self.__fuel_type = fuel_type

    @property
    def fuel_type(self):
        return self.__fuel_type
    
    def start(self):
        print(f'I am starting the engine')

    def stop(self):
        print(f'I am starting the engine')

    def get_state(self):
        print(f'Returning state')