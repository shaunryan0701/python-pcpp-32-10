from delicacy import Delicacy
from copy import copy
from copy import deepcopy

'''
Introduce the Delicacy class to represent a generic delicacy. 
  The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
Your class should implement the __str__() method to represent each object state;
Experiment with the copy.copy() and deepcopy.copy() methods 
  to see the difference in how each method copies objects .
'''

lollypop = Delicacy('Lolly Pop', 0.4, 133)
licorice = Delicacy('Licorice', 0.1, 251)
chocolate = Delicacy('Chocolate', 1, 601)
sours = Delicacy('Sours', 0.01, 513)
hard_candies = Delicacy('Hard candies', 0.3, 433)

warehouse = [lollypop, licorice, chocolate, sours, hard_candies]
print('Source list of candies')
for item in warehouse:
    print(item, id(item))

print('Copied list of candies')
warehouse_copy = copy(warehouse)
for item in warehouse_copy:
    print(item, id(item))

print("\nUpdate price of lolly pop\n")
warehouse[0].price = 0.444
print('Source list of candies')
for item in warehouse:
    print(item, id(item))

print('Copied list of candies')
for item in warehouse_copy:
    print(item, id(item))

print('\nDeep Copied list of candies')
warehouse_copy = deepcopy(warehouse)
for item in warehouse_copy:
    print(item, id(item))

print("\nUpdate price of lolly pop\n")
warehouse[0].price = 0.888
print('Source list of candies')
for item in warehouse:
    print(item, id(item))

print('Deep Copied list of candies')
for item in warehouse_copy:
    print(item, id(item))