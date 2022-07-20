from src.__Parents.Controller import Controller
from .IncomeService import IncomeService
from .IncomeRepository import IncomeRepository
from src.Firm.FirmRepository import FirmRepository
from src.IncomeType.IncomeTypeRepository import IncomeTypeRepository
from src.Colleague.ColleagueRepository import ColleagueRepository
from src.Product.ProductRepository import ProductRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .IncomeValidator import income_schema


class IncomeController(Controller):
    income_service: IncomeService = IncomeService(
        income_repository=IncomeRepository(),
        colleague_repository=ColleagueRepository(),
        income_type_repository=IncomeTypeRepository(),
        firm_repository=FirmRepository(),
        product_repository=ProductRepository())

    # POST
    @expects_json(income_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('income_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.income_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(income_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('income_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.income_service.update(body=self.request.get_json(), income_id=self.id)
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('income_edit')
    def delete(self) -> dict:
        res: dict = self.income_service.delete(income_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('income_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.income_service.get_by_id(income_id=self.id)
        else:
            res: dict = self.income_service.get_all(page=self.page,
                                                    per_page=self.per_page,
                                                    firm_id=self.arguments.get('firm_id'))
        return res
