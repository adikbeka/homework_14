'''
Task 2

Notification
'''

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, address: str, text: str):
        self.address = address
        self.text = text

    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print(f'Email has been sent to: {self.address}, text: {self.text}')


class SmsNotification(Notification):
    def send(self):
        print(f'SMS has been sent to: {self.address}, text: {self.text}')


class PushNotification(Notification):
    def send(self):
        print(f'Push Notification has been sent to: {self.address}, text: {self.text}')


notifications = [
    EmailNotification("email@example.com", "Привет!"),
    SmsNotification("+123456789", "Новый SMS!"),
    PushNotification("user_123", "Новое уведомление!")
]

for notification in notifications:
    notification.send()
