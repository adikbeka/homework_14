'''
Homework 2, part 3
'''

# Part 3

class A:
    def perform(self):
        print('Performing actions of A')


class B(A):
    def perform(self):
        print('Performing actions of B')


class C(A):
    def perform(self):
        print('Performing actions of C')


class D(B, C):
    def perform(self):
        pass


d = D()

d.perform()

print(D.__mro__)


