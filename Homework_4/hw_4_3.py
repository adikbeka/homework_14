'''
Task 2

Data storage
'''

from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, text: str):
        pass


class DatabaseStorage(Storage):
    def save(self, text: str):
        print(f'Data has been saved in Database')


class FileStorage(Storage):
    def save(self, text: str):
        print(f'Data has been saved in File')


class DataService:
    def __init__(self, storage: Storage):
        self.storage = storage

    def save_data(self, text: str):
        self.storage.save(text)


db_storage = DatabaseStorage()
file_storage = FileStorage()

data_service = DataService(db_storage)
data_service.save_data("Сохраняем в базу данных")

data_service = DataService(file_storage)
data_service.save_data("Сохраняем в файл")