from src.__Parents.Repository import Repository
from .IIncomeRepo import IIncomeRepo
from .IncomeModel import Income
from flask import g


class IncomeRepository(Repository, IIncomeRepo):
    income: Income = Income

    def create(self, body: dict, client_id: int):
        income = self.income()
        income.price = body['price']
        income.count = body['count']
        income.income_type_id = body['income_type_id']
        income.product_id = body['product_id']
        income.firm_id = body['firm_id']
        income.client_id = client_id
        income.save_db()

    def update(self, income: Income, body: dict):
        income.price = body['price']
        income.count = body['count']
        income.income_type_id = body['income_type_id']
        income.product_id = body['product_id']
        income.firm_id = body['firm_id']
        income.update_db()

    def delete(self, income: Income):
        income.delete_db()

    def get_by_id(self, income_id: int) -> Income:
        income = self.income.query.filter_by(id=income_id, client_id=g.client_id)\
            .filter(self.income.firm_id.in_(g.allowed_firm_ids)).first()
        return income

    def get_all(self, page: int, per_page: int, firm_id: int or None) -> dict:
        incomes = self.income.query.filter_by(client_id=g.client_id)\
            .filter(self.income.firm_id.in_(g.allowed_firm_ids))\
            .filter(self.income.firm_id == firm_id if firm_id else self.income.firm_id.isnot(None))\
            .paginate(page=page, per_page=per_page)
        return self.get_page_items(incomes)
