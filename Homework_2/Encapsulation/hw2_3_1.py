'''
Homework 2_3, Part 1 and 2
'''

# Part 1

class Device:
    def __init__(self, temperature = 20):
        self.__temperature = temperature

    def inrease_temperature(self, degree):
        if self.__temperature + degree > 80:
            print('Temperature is above 80')
        else:
            self.__temperature += degree
    def decrease_temperature(self, degree):
        if self.__temperature + degree <= 0:
            print('Temperature is below 0')
        else:
            self.__temperature -= degree

    def get_temperature(self):
        return self.__temperature


device = Device()

device.inrease_temperature(10)
print(f'Increased temperature: {device.get_temperature()}')

device.decrease_temperature(10)
print(f'Decreased temperature: {device.get_temperature()}')



# Part 2

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        balance = self.__get_balance()
        print(f'Баланс: {self.__balance}')
        if amount > 0:
            self.__balance += amount
            print(f"{amount} добавлено на счет")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        comissions = (amount * 2 / 100)
        if 0 < amount <= self.__balance:
            self.__balance -= amount + comissions
            print(f"{amount + comissions} снято со счета")
        else:
            print("Недостаточно средств или неверная сумма")

    def get_balance(self):
        return self.__balance

    def __get_balance(self):
        pass


bank_account = BankAccount(1000)


bank_account.deposit(200)
current_balance = bank_account.get_balance()
print(f'Current balance: {current_balance}')

bank_account.withdraw(200)
current_balance = bank_account.get_balance()
print(f'Current balance: {current_balance}')
