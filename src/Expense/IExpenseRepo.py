from abc import ABC, abstractmethod
from .ExpenseModel import Expense


class IExpenseRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, expense: Expense, body: dict):
        pass

    @abstractmethod
    def delete(self, expense: Expense):
        pass

    @abstractmethod
    def get_by_id(self, expense_id: int) -> Expense:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, firm_id: int or None) -> dict:
        pass
