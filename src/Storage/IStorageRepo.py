from abc import ABC, abstractmethod
from src.Storage.StorageModel import Storage


class IStorageRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, storage: Storage, body: dict):
        pass

    @abstractmethod
    def delete(self, storage: Storage):
        pass

    @abstractmethod
    def get_by_id(self, storage_id: int) -> Storage:
        pass

    @abstractmethod
    def get_by_code(self, code: str) -> Storage:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, firm_id: int or None, search: str or None):
        pass
