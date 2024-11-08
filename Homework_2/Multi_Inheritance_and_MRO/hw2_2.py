'''
Homework 2, part 2
'''



# Part 2

class Person:
    def introduce(self, name):
        self.name = name
        print(f'Hello {self.name}')


class Worker:
    def worker(self):
        print('Working')


class Student:
    def study(self):
        print('Learning a new topic')


class Intern(Worker, Student):
    def daily_schedule(self):
        return self.worker(), self.study()


intern = Intern()

intern.daily_schedule()


