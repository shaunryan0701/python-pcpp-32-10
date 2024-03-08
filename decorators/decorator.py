def decorator(func):
    def wrapper():
        print('Some action before the function')
        func()
        print('Some action after the function')
    return wrapper

# def say_whee():
#     print('Whee!')

# say_whee = decorator(say_whee)

@decorator
def say_whee():
    print('Whee!')
