'''
Homework 2_4, Part 2
'''


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 1.8) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9


temperature = TemperatureConverter
to_fahrenheit = temperature.celsius_to_fahrenheit(30)
print(f'Converting from celsius to fahrenheit: {to_fahrenheit}')

to_celsius = temperature.fahrenheit_to_celsius(60)
print(f'Converting from fahrenheit to celsius: {to_celsius}')