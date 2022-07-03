from src.__Parents.Controller import Controller
from .ExpenseTypeRepository import ExpenseTypeRepository
from .ExpenseTypeService import ExpenseTypeService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .ExpenseTypeValidator import expense_type_schema
from src.Permission.PermissionMiddleware import PermissionMiddleware


class ExpenseTypeController(Controller):
    expense_type_service: ExpenseTypeService = ExpenseTypeService(ExpenseTypeRepository())

    # POST
    @expects_json(expense_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('expense_type_edit')
    def post(self) -> dict:
        res: dict = self.expense_type_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(expense_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('expense_type_edit')
    def put(self) -> dict:
        res: dict = self.expense_type_service.update(expense_type_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('expense_type_edit')
    def delete(self) -> dict:
        res: dict = self.expense_type_service.delete(expense_type_id=self.id)
        return res

    # GET
    def get(self) -> dict:
        if self.id:
            res: dict = self.expense_type_service.get_by_id(self.id)
        else:
            res: dict = self.expense_type_service.get_all()
        return res
