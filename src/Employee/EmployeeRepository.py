from .IEmployeeRepo import IEmployeeRepo
from src.__Parents.Repository import Repository
from .EmployeeModel import Employee
from flask import g


class EmployeeRepository(Repository, IEmployeeRepo):
    employee: Employee = Employee

    def create(self, body: dict):
        employee = self.employee()
        employee.title = body['title']
        employee.code = body['code']
        employee.position = body['position']
        employee.adoption_date = body['adoption_date']
        employee.birth_date = body['birth_date']
        employee.employee_bank_account = body['employee_bank_account']
        employee.social_card = body['social_card']
        employee.passport_number = body['passport_number']
        employee.phone_number = body['phone_number']
        employee.firm_id = body['firm_id']
        employee.client_id = g.client_id
        employee.save_db()

    def update(self, employee: Employee, body: dict):
        employee.title = body['title']
        employee.code = body['code']
        employee.position = body['position']
        employee.adoption_date = body['adoption_date']
        employee.birth_date = body['birth_date']
        employee.employee_bank_account = body['employee_bank_account']
        employee.social_card = body['social_card']
        employee.passport_number = body['passport_number']
        employee.phone_number = body['phone_number']
        employee.firm_id = body['firm_id']
        employee.update_db()

    def delete(self, employee: Employee):
        employee.delete_db()

    def get_by_id(self, employee_id: int) -> Employee:
        employee = self.employee.query.filter(Employee.firm_id.in_(g.allowed_firm_ids),
                                              Employee.id == employee_id,
                                              Employee.client_id == g.client_id).first()
        employee.firm = employee.firm
        return employee

    def get_all(self, page: int, per_page: int, code: int or None, firm_id: int or None) -> dict:
        employees = self.employee.query.filter_by(client_id=g.client_id)\
            .filter(Employee.firm_id.in_(g.allowed_firm_ids))\
            .filter(self.employee.code == code if code else self.employee.code.isnot(None),
                    self.employee.firm_id == firm_id if firm_id else self.employee.firm_id.isnot(None))\
            .paginate(page=page, per_page=per_page)

        for employee in employees.items:
            employee.firm = employee.firm

        return self.get_page_items(employees)
