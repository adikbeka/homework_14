'''
Homework 1, part 2
'''


# Part 2

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f'Vehicle is started moving')

class Car(Vehicle):
    def move(self):
        print(f'Car is started moving with {self.speed} km/h')


class Bicycle(Vehicle):
    def move(self):
        print(f'Bicycle is started moving with {self.speed} km/h')


car = Car(100)
bicycle = Bicycle(15)

car.move()
bicycle.move()



