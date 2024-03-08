from decorators import do_twice
from decorators import timer, debug, slow_down
from decorators_with_arguments import repeat

@do_twice
def say_whee():
    print('Whee!')


@do_twice
def greet(name):
    print('Preparing greeting')
    return f'Hello {name}!'

@debug
@timer
def waste_some_time(num_times, pointless=True):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(1000, pointless=False)

@slow_down
def countdown(from_number):
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1)

countdown(3)

@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

greet('Geoff')