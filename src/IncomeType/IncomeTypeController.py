from src.__Parents.Controller import Controller
from .IncomeTypeRepository import IncomeTypeRepository
from .IncomeTypeService import IncomeTypeService
from src.Auth.AuthMiddleware import AuthMiddleware
from flask_expects_json import expects_json
from .IncomeTypeValidator import income_type_schema
from src.Permission.PermissionMiddleware import PermissionMiddleware


class IncomeTypeController(Controller):
    income_type_service: IncomeTypeService = IncomeTypeService(IncomeTypeRepository())

    # POST
    @expects_json(income_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('income_type_edit')
    def post(self) -> dict:
        res: dict = self.income_type_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(income_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('income_type_edit')
    def put(self) -> dict:
        res: dict = self.income_type_service.update(income_type_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('income_type_edit')
    def delete(self) -> dict:
        res: dict = self.income_type_service.delete(income_type_id=self.id)
        return res

    # GET
    def get(self) -> dict:
        if self.id:
            res: dict = self.income_type_service.get_by_id(self.id)
        else:
            res: dict = self.income_type_service.get_all()
        return res
