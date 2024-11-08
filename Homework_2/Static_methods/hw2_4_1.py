'''
Homework 2_4, Part 1
'''


# Part 1

class TimeUtils:
    @staticmethod
    def is_morning(hour):
        return 6 <= hour <= 12


time = TimeUtils

result = time.is_morning(11)
print(f'Is 11 is morning? {result}')