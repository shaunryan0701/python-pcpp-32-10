from engine import Engine
from tire import Tyre

class Car():
    def __init__(self, VIN, engine: Engine, tyres: list[Tyre]) -> None:
        self._VIN = VIN
        self.engine = engine
        self.tyres = tyres

    @property
    def VIN(self):
        return self._VIN



