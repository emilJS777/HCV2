from abc import ABC, abstractmethod
from .UnitModel import Unit


class IUnitRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, unit: Unit, body: dict):
        pass

    @abstractmethod
    def delete(self, unit: Unit):
        pass

    @abstractmethod
    def get_by_id(self, unit_id: int) -> Unit:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Unit:
        pass

    @abstractmethod
    def get_all(self) -> dict:
        pass
