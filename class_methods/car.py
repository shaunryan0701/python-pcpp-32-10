class Car:
  def __init__(self, vin):
    print('Ordinary __init__ was called for', vin)
    self.vin = vin
    self.brand = ''

  @classmethod
  def including_brand(cls, vin, brand):
    print(f'Class method including_brand called : {brand}')
    _car = cls(vin)
    _car.brand = brand
    return _car