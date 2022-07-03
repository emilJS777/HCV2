from abc import ABC, abstractmethod
from .ColleagueModel import Colleague


class IColleagueRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, colleague: Colleague, body: dict):
        pass

    @abstractmethod
    def delete(self, colleague: Colleague):
        pass

    @abstractmethod
    def get_by_id(self, colleague_id: int, client_id: int) -> Colleague:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, client_id: int) -> dict:
        pass

    @abstractmethod
    def get_by_title(self, title: str, client_id: int) -> Colleague:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, colleague_id: int, title: str, client_id: int) -> Colleague:
        pass
