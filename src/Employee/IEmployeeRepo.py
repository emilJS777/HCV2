from abc import ABC, abstractmethod
from .EmployeeModel import Employee


class IEmployeeRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, employee: Employee, body: dict):
        pass

    @abstractmethod
    def delete(self, employee: Employee):
        pass

    @abstractmethod
    def get_by_id(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, search: str or None, firm_id: int or None) -> dict:
        pass
