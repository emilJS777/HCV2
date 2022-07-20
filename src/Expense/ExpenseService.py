from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IExpenseRepo import IExpenseRepo
from flask import g
from src.Firm.IFirmRepo import IFirmRepo
from src.Colleague.IColleagueRepo import IColleagueRepo
from src.ExpenseType.IExpenseTypeRepo import IExpenseTypeRepo


class ExpenseService(Service, Repository):
    def __init__(self, expense_repository: IExpenseRepo,
                 firm_repository: IFirmRepo,
                 colleague_repository: IColleagueRepo,
                 expense_type_repository: IExpenseTypeRepo):

        self.expense_repository: IExpenseRepo = expense_repository
        self.firm_repository: IFirmRepo = firm_repository
        self.colleague_repository: IColleagueRepo = colleague_repository
        self.expense_type_repository: IExpenseTypeRepo = expense_type_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found('коллега не найдена')

        if not self.expense_type_repository.get_by_id(expense_type_id=body['expense_type_id']):
            return self.response_not_found('тип траты не найден')

        self.expense_repository.create(body=body, client_id=g.client_id)
        return self.response_created('трата создана')

    # UPDATE
    def update(self, body: dict, expense_id: int) -> dict:
        expense = self.expense_repository.get_by_id(expense_id=expense_id)
        if not expense:
            return self.response_not_found('трата не найдена')

        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        if not self.colleague_repository.get_by_id(colleague_id=body['colleague_id'], client_id=g.client_id):
            return self.response_not_found('коллега не найдена')

        if not self.expense_type_repository.get_by_id(expense_type_id=body['expense_type_id']):
            return self.response_not_found('тип траты не найден')

        self.expense_repository.update(expense=expense, body=body)
        return self.response_updated('трата обновлена')

    # DELETE
    def delete(self, expense_id: int) -> dict:
        expense = self.expense_repository.get_by_id(expense_id=expense_id)
        if not expense:
            return self.response_not_found('трата не найдена')

        self.expense_repository.delete(expense)
        return self.response_deleted('трата удалена')

    # GET BY ID
    def get_by_id(self, expense_id: int) -> dict:
        expense = self.expense_repository.get_by_id(expense_id=expense_id)
        if not expense:
            return self.response_not_found('трата не найдена')

        return self.response_ok(self.get_dict_items(expense))

    # GET ALL
    def get_all(self, page: int, per_page: int, firm_id: int or None) -> dict:
        expenses = self.expense_repository.get_all(page=page, per_page=per_page, firm_id=firm_id)
        return self.response_ok(expenses)

    