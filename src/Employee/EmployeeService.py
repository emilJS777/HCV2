from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IEmployeeRepo import IEmployeeRepo
from ..Firm.IFirmRepo import IFirmRepo
from flask import g


class EmployeeService(Service, Repository):

    def __init__(self, employee_repository: IEmployeeRepo, firm_repository: IFirmRepo):
        self.employee_repository: IEmployeeRepo = employee_repository
        self.firm_repository: IFirmRepo = firm_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        self.employee_repository.create(body=body)
        return self.response_created('работник создан')

    # UPDATE
    def update(self, employee_id: int, body: dict) -> dict:
        employee = self.employee_repository.get_by_id(employee_id)
        if not employee:
            return self.response_not_found('работник не найден')

        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        self.employee_repository.update(employee=employee, body=body)
        return self.response_updated('работник обновлен')

    # DELETE
    def delete(self, employee_id: int) -> dict:
        employee = self.employee_repository.get_by_id(employee_id)
        if not employee:
            return self.response_not_found('работник не найден')

        self.employee_repository.delete(employee)
        return self.response_deleted('работник удален')

    # GET BY ID
    def get_by_id(self, employee_id: int) -> dict:
        employee = self.employee_repository.get_by_id(employee_id)
        if not employee:
            return self.response_not_found('работник не найден')

        return self.response_ok(self.get_dict_items(employee))

    # GET ALL
    def get_all(self, page: int, per_page: int, code: int or None, firm_id: int or None) -> dict:
        employees = self.employee_repository.get_all(
            page=page,
            per_page=per_page,
            code=code,
            firm_id=firm_id)

        return self.response_ok(employees)
    