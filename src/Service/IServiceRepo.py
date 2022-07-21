from abc import ABC, abstractmethod
from .ServiceModel import Service


class IServiceRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, service: Service, body: dict):
        pass

    @abstractmethod
    def delete(self, service: Service):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str or None, client_id: int) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, service_id: int, client_id: int) -> Service:
        pass

    @abstractmethod
    def get_by_title(self, title: str, client_id: int) -> Service:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, service_id: int, title: str, client_id: int) -> Service:
        pass

    @abstractmethod
    def get_by_code(self, code: str, client_id: int) -> Service:
        pass

    @abstractmethod
    def get_by_code_exclude_id(self, service_id: int, code: str, client_id: int) -> Service:
        pass

