'''
Homework 2_2, Part 1 and 2
'''

# Part 1

from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def charge(self):
        pass


class Phone(Device):
    def charge(self):
        print('Charging by using USB')


class Laptop(Device):
    def charge(self):
        print('Charging via power adapter')


class WirelessEarbuds(Device):
    def charge(self):
        print('Charging via wireless charger')


def charge_devices(device: Device):
    device.charge()


devices = [Phone(), Laptop(), WirelessEarbuds()]

for device in devices:
    charge_devices(device)



# Part 2

class Employee(ABC):
    @abstractmethod
    def perform_task(self):
        pass


class Developer(Employee):
    def perform_task(self):
        print('Writing a code')


class Designer(Employee):
    def perform_task(self):
        print('Creating a layout')


class Manager(Employee):
    def perform_task(self):
        print('Holding a meeting')


def work_day(employees: Employee):
    employees.perform_task()

employees = [Developer(), Designer(), Manager()]

for employee in employees:
    work_day(employee)

