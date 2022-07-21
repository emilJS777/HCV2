from abc import ABC, abstractmethod


class IFirmRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, firm_id: int, body: dict):
        pass

    @abstractmethod
    def delete(self, firm_id: int):
        pass

    @abstractmethod
    def get_by_id(self, firm_id: int, client_id: int) -> dict:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str or None, sphere_id: int or None, client_id: int) -> dict:
        pass

    @abstractmethod
    def get_by_title(self, title: str, client_id: int):
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, firm_id: int, title: str, client_id: int):
        pass
