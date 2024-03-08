from engine import Engine
from car import Car
from tire import Tyre

city_engine = Engine('Electric')

car = Car('BOLLOX', city_engine, [Tyre(15) for _ in range(4)])

print(car.__dict__)
car.engine.start()
print(car.tyres[0].pressure)
car.tyres[1].pressure = 40
car.tyres[2].pump()