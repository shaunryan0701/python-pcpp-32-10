class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
         return f"{{'name': {self.name} 'price': {self.price}, 'weight': {self.weight}}}"
