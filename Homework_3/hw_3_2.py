'''
Task 1. Has been done by my Tutor "ChatGPT". Didn't understand this theme at all
'''


class Developer:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_info(self):
        tasks_info = '\n '.join(self.tasks) if self.tasks else 'No tasks assigned'
        print(f'Developer: {self.name}\n Tasks: {tasks_info}')


class Project:
    def __init__(self, title):
        self.title = title
        self.developers = []

    def add_developer(self, developer):
        self.developers.append(developer)
        print(f'Developer {developer.name} has been added to the project {self.title}')

    def assign_task(self, developer_name, task):
        for developer in self.developers:
            if developer_name == developer.name:
                developer.add_task(task)

                print(f'TasK {task} has been assigned to {developer_name}')
                return
        print(f'Developer with name {developer_name} not found in the project')

    def get_project_info(self):
        print(f'Project: {self.title}')

        if not self.developers:
            print('No developers assigned to this project')

        for developer in self.developers:
            print(developer.get_info())
            print('-' * 15)


project = Project("Новый проект")
dev1 = Developer("Alice")
dev2 = Developer("Bob")

project.add_developer(dev1)
project.add_developer(dev2)

# Назначение задач
project.assign_task("Alice", "Fix bug #101")
project.assign_task("Bob", "Implement feature X")

# Вывод информации о проекте

project.get_project_info()