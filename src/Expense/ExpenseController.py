from src.__Parents.Controller import Controller
from .ExpenseService import ExpenseService
from .ExpenseRepository import ExpenseRepository
from src.Firm.FirmRepository import FirmRepository
from src.ExpenseType.ExpenseTypeRepository import ExpenseTypeRepository
from src.Colleague.ColleagueRepository import ColleagueRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .ExpenseValidator import expense_schema


class ExpenseController(Controller):
    expense_service: ExpenseService = ExpenseService(
        expense_repository=ExpenseRepository(),
        colleague_repository=ColleagueRepository(),
        expense_type_repository=ExpenseTypeRepository(),
        firm_repository=FirmRepository())

    # POST
    @expects_json(expense_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('expense_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.expense_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(expense_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('expense_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.expense_service.update(body=self.request.get_json(), expense_id=self.id)
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('expense_edit')
    def delete(self) -> dict:
        res: dict = self.expense_service.delete(expense_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('expense_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.expense_service.get_by_id(expense_id=self.id)
        else:
            res: dict = self.expense_service.get_all(page=self.page,
                                                     per_page=self.per_page,
                                                     firm_id=self.arguments.get('firm_id'))
        return res
