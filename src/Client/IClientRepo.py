from abc import ABC, abstractmethod


class IClientRepo(ABC):

    @abstractmethod
    def create(self, body: dict, parent_id: int or None):
        pass

    @abstractmethod
    def get_by_id(self, client_id: int, parent_id: int):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, parent_id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str, parent_id: int or None):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, client_id: int, name: str, parent_id: int):
        pass
