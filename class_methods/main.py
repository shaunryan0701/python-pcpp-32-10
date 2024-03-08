from example import Example
from car import Car

print (Example.get_internal())

ex1 = Example(1)
print (Example.get_internal())

ex2 = Example(2)
print (Example.get_internal())

car1 = Car('1234')
car2 = Car.including_brand('5678', 'Toyota')

print (car1.vin, car1.brand)
print (car2.vin, car2.brand)