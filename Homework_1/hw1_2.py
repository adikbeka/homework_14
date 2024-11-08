'''
Homework 2, 1 and 2 part
'''

# Part 1

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, length):  # Changed height to length
        self.width = width
        self.length = length

    def area(self):
        print(f'Area of rectangle: {self.width * self.length}')

    def perimeter(self):
        print(f'Perimeter of rectangle: {(self.width + self.length) * 2}')


rectangle = Rectangle(2, 3)
rectangle.area()

rectangle.perimeter()


# Part 2

class Appliance:
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class WashingMachine(Appliance):
    def turn_on(self):
        print('Washing Machine is turned on')

    def turn_off(self):
        print('Washing Machine is turned off')


class Refrigerator(Appliance):
    def turn_on(self):
        print('Refrigerator is turned on')

    def turn_off(self):
        print('Refrigerator is turned off')


washing_machine = WashingMachine()
refrigerator = Refrigerator()

washing_machine.turn_on()
washing_machine.turn_off()

refrigerator.turn_on()
refrigerator.turn_off()
