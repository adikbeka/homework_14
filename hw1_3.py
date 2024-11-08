'''
Homework 3, part 1 and 2
'''

# Part 1

class Car:
    def __init__(self, color: str, fuel: str, currency: str):
        self.color = color
        self.fuel = fuel
        self.company = 'Astana Motors'
        self.currency = currency
        self.price = 20000000

        print('Car is created')

    def go(self, speed: int = 100):
        print('Car is driving with speed: ',speed)
        self.info()

    def stop(self):
        print('Car is stopped')

    def beep(self):
        print('Beeeeeeep')

    def info(self):
        print(f'Color of the car {self.color} and using a {self.fuel}')

    @property # Using it in a big logic and allows to address as a variable
    def converted_price(self):
        if self.currency == 'USD':
            return self.price // 487
        elif self.currency == 'EUR':
            return self.price // 550
        elif self.currency == 'GBP':
            return self.price // 635
        elif self.currency == 'CNY':
            return self.price // 68
        else:
            return self.price


mercedes = Car('White', 'Gas', 'GBP')
bmw = Car('Black', 'Petrol', 'CNY')
mercedes.go(30)
mercedes.go(60)


print(mercedes.converted_price)
print(bmw.converted_price)



# Part 2

class Product:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    @property
    def final_price(self):
        print(f'Price of the Product with discount: {self.price * (1 - self.discount / 100)}')


product1 = Product(1000, 20)
product2 = Product(3992, 35)
product3 = Product(15000, 23)

product1.final_price
product2.final_price
product3.final_price
