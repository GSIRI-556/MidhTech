def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorator  #greet = my_decorator(greet)
def greet():
    print("Hello")
greet()