'''
Task 1
'''


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f'User: {user} has been added')

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f'User: {user} removed from users')
        else:
            print(f'Such user {user} not found')

    def get_user(self, name):
        for user in self.users:
            if user == name:
                return user
        return None


class Notifier:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager

    def send_notification(self, user_name, text: str):
        user = self.user_manager.get_user(user_name)
        if user:
            print(f'Notification has been sent to {user}, Text: {text}')
        else:
            print(f'User {user} not found and notification not sent')


manager = UserManager()
notifier = Notifier(manager)

manager.add_user("Alice")
manager.add_user("Bob")

notifier.send_notification("Alice", "Добро пожаловать!")
notifier.send_notification("Bob", "У вас новое сообщение")
notifier.send_notification("Charlie", "Hello!")