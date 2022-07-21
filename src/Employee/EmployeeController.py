from src.__Parents.Controller import Controller
from .EmployeeService import EmployeeService
from .EmployeeRepository import EmployeeRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .EmployeeValidator import employee_schema
from src.Firm.FirmRepository import FirmRepository


class EmployeeController(Controller):
    employee_service: EmployeeService = EmployeeService(EmployeeRepository(), FirmRepository())

    # POST
    @expects_json(employee_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('employee_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.employee_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(employee_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('employee_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.employee_service.update(
            employee_id=self.id,
            body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('employee_edit')
    def delete(self) -> dict:
        res: dict = self.employee_service.delete(self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('employee_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.employee_service.get_by_id(self.id)
        else:
            res: dict = self.employee_service.get_all(
                page=self.page,
                per_page=self.per_page,
                search=self.arguments.get('search'),
                firm_id=self.arguments.get('firm_id'))
        return res
