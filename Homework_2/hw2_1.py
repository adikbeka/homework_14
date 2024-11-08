'''
Homework 2, part 1
'''

# Part 1

class Walker:
    def walk(self):
        print('Can walk')


class Swimmer:
    def swim(self):
        print('Can swim')


class Flyer:
    def fly(self):
        print('Can fly')


class Duck(Walker, Swimmer):
    pass
    # print('Duck is walking and swimming')


class Penguin(Walker, Swimmer):
    pass
    # print('Penguin is walking and swimming')


class SuperHero(Walker, Swimmer, Flyer):
    pass
    # print('Superhero is walking, swimming and flying')


duck = Duck()
penguin = Penguin()
superhero = SuperHero()

duck.walk()
duck.swim()

penguin.walk()
penguin.swim()

superhero.walk()
superhero.swim()
superhero.fly()



