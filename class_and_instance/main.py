from chicken import Chicken
from duck import Duck

duckling = Duck(height=10, weight=3.4, sex="male")
drake = Duck(height=25, weight=3.7, sex="male")
hen = Duck(height=20, weight=3.4, sex="female")

chicken = Chicken()

print('So many ducks were born:', Duck.counter)

def output():
  for poultry in duckling, drake, hen, chicken:
      print(poultry.species, end=' ')
      if poultry.species == 'duck':
          poultry.quack()
      elif poultry.species == 'chicken':
          poultry.cluck()

output()