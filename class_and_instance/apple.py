import random

class Apple:
    count = 0
    total_weight = 0
    
    def __init__(self):
        Apple.count += 1
        self.weight = random.uniform(0.3, 0.5)
        Apple.total_weight += self.weight
        
while Apple.count <= 1000 and Apple.total_weight < 300.0:
    
    apple = Apple()
    print(Apple.count, "apple(s) selected", apple.weight)
    
print(Apple.count)
print(Apple.total_weight)