from abc import ABC, abstractmethod
from .IncomeTypeModel import IncomeType


class IIncomeTypeRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, income_type: IncomeType, body: dict):
        pass

    @abstractmethod
    def delete(self, income_type: IncomeType):
        pass

    @abstractmethod
    def get_by_id(self, income_type_id: int) -> IncomeType:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> IncomeType:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, title: str, income_type_id: int) -> IncomeType:
        pass
