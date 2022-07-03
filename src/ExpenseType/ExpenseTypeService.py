from .IExpenseTypeRepo import IExpenseTypeRepo
from ..__Parents.Service import Service


class ExpenseTypeService(Service):
    def __init__(self, expense_type_repository: IExpenseTypeRepo):
        self.expense_type_repository: IExpenseTypeRepo = expense_type_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.expense_type_repository.get_by_title(body['title']):
            return self.response_conflict('тип расходов уже существует')

        self.expense_type_repository.create(body)
        return self.response_created('тип расходов создан')

    # UPDATE
    def update(self, expense_type_id: int, body: dict) -> dict:
        expense_type = self.expense_type_repository.get_by_id(expense_type_id)

        if not expense_type:
            return self.response_not_found('тип расходов не найден')

        if self.expense_type_repository.get_by_title_exclude_id(title=body['title'], expense_type_id=expense_type_id):
            return self.response_conflict('тип расходов по такому названию уже существует')

        self.expense_type_repository.update(expense_type=expense_type, body=body)
        return self.response_updated('тип расходов обновлен')

    # DELETE
    def delete(self, expense_type_id: int) -> dict:
        expense_type = self.expense_type_repository.get_by_id(expense_type_id)
        if not expense_type:
            return self.response_not_found('тип расходов не найден')

        self.expense_type_repository.delete(expense_type)
        return self.response_deleted('тип расходов удален')

    # GET BY ID
    def get_by_id(self, expense_type_id: int) -> dict:
        expense_type = self.expense_type_repository.get_by_id(expense_type_id)
        if not expense_type:
            return self.response_not_found('тип расходов не найден')

        return self.response_ok({'id': expense_type.id,
                                 'title': expense_type.title,
                                 'description': expense_type.description})

    # GET ALL
    def get_all(self) -> dict:
        expense_types = self.expense_type_repository.get_all()
        return self.response_ok(expense_types)
