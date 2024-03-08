from tank import Tank, TankException

tank1 = Tank(100)
print('Current liquid level:', tank1.level)

tank1.level = 50
print('Current liquid level:', tank1.level)

tank1.level += 10
print('Current liquid level:', tank1.level)
print('Current liquid capacity:', tank1.capacity)

try:  
  tank1.level = 101
except TankException as e:
  print(f'Trying to set liquid level to {tank1.level + 100} units, result:', e)
except Exception as e:
  print('Trying to set liquid level to 21 units, result:', e)