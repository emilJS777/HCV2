from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IIncomeRepo import IIncomeRepo
from flask import g
from src.Firm.IFirmRepo import IFirmRepo
from src.Colleague.IColleagueRepo import IColleagueRepo
from src.IncomeType.IIncomeTypeRepo import IIncomeTypeRepo
from src.Product.IProductRepo import IProductRepo


class IncomeService(Service, Repository):
    def __init__(self, income_repository: IIncomeRepo,
                 firm_repository: IFirmRepo,
                 colleague_repository: IColleagueRepo,
                 income_type_repository: IIncomeTypeRepo,
                 product_repository: IProductRepo):

        self.income_repository: IIncomeRepo = income_repository
        self.firm_repository: IFirmRepo = firm_repository
        self.colleague_repository: IColleagueRepo = colleague_repository
        self.income_type_repository: IIncomeTypeRepo = income_type_repository
        self.product_repository: IProductRepo = product_repository

    # CRAETE
    def create(self, body: dict) -> dict:
        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found('коллега не найдена')

        if not self.income_type_repository.get_by_id(income_type_id=body['income_type_id']):
            return self.response_not_found('тип прибыли не найден')

        if not self.product_repository.get_by_id(product_id=body['product_id'], client_id=g.client_id):
            return self.response_not_found('продукт не найден')

        self.income_repository.create(body=body, client_id=g.client_id)
        return self.response_created('прибыль создана')

    # UPDATE
    def update(self, body: dict, income_id: int) -> dict:
        income = self.income_repository.get_by_id(income_id=income_id)
        if not income:
            return self.response_not_found('прибыль не найдена')

        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found('коллега не найдена')

        if not self.income_type_repository.get_by_id(income_type_id=body['income_type_id']):
            return self.response_not_found('тип прибыли не найден')

        if not self.product_repository.get_by_id(product_id=body['product_id'], client_id=g.client_id):
            return self.response_not_found('продукт не найден')

        self.income_repository.update(income=income, body=body)
        return self.response_updated('прибыль обновлена')

    # DELETE
    def delete(self, income_id: int) -> dict:
        income = self.income_repository.get_by_id(income_id=income_id)
        if not income:
            return self.response_not_found('прибыль не найдена')

        self.income_repository.delete(income)
        return self.response_deleted('прибыль удалена')

    # GET BY ID
    def get_by_id(self, income_id: int) -> dict:
        income = self.income_repository.get_by_id(income_id=income_id)
        if not income:
            return self.response_not_found('прибыль не найдена')

        return self.response_ok(self.get_dict_items(income))

    # GET ALL
    def get_all(self, page: int, per_page: int, firm_id: int or None) -> dict:
        incomes = self.income_repository.get_all(page=page, per_page=per_page, firm_id=firm_id)
        return self.response_ok(incomes)

    