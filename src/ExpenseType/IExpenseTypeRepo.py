from abc import ABC, abstractmethod
from .ExpenseTypeModel import ExpenseType


class IExpenseTypeRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, expense_type: ExpenseType, body: dict):
        pass

    @abstractmethod
    def delete(self, expense_type: ExpenseType):
        pass

    @abstractmethod
    def get_by_id(self, expense_type_id: int) -> ExpenseType:
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> ExpenseType:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, title: str, expense_type_id: int) -> ExpenseType:
        pass
