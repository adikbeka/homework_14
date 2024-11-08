'''
Homework 2, part 4
'''

# Part 4

class Artist:
    def draw(self):
        print('Painting a picture')


class Musician:
    def play(self):
        print('Playing an instrument')


class CreativePerson(Artist, Musician):
    def inspire(self):
        print('Inspiring by art')


creative_person = CreativePerson()

creative_person.draw()
creative_person.play()
creative_person.inspire()