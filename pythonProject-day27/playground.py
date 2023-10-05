import tkinter

def add(*args):
    sum = 0
    for n in args:
        sum +=  n

    return sum

print(add(3, 5, 6, 7, 8, 4, 2))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])

    n += kwargs["add"]
    n +=kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

my_car = Car(make="nissan")

print(my_car.model)
print(my_car.make)