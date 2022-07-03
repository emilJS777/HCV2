from .IExpenseTypeRepo import IExpenseTypeRepo
from src.__Parents.Repository import Repository
from .ExpenseTypeModel import ExpenseType


class ExpenseTypeRepository(Repository, IExpenseTypeRepo):
    expense_type: ExpenseType = ExpenseType

    def create(self, body: dict):
        expense_type = self.expense_type()
        expense_type.title = body['title']
        expense_type.description = body['description']
        expense_type.save_db()

    def update(self, expense_type: ExpenseType, body: dict):
        expense_type.title = body['title']
        expense_type.description = body['description']
        expense_type.update_db()

    def delete(self, expense_type: ExpenseType):
        expense_type.delete_db()

    def get_by_id(self, expense_type: int) -> ExpenseType:
        expense_type = self.expense_type.query.filter_by(id=expense_type).first()
        return expense_type

    def get_by_title(self, title: str) -> ExpenseType:
        expense_type = self.expense_type.query.filter_by(title=title).first()
        return expense_type

    def get_all(self):
        expense_types = self.expense_type.query.all()
        return self.get_array_items(expense_types)

    def get_by_title_exclude_id(self, title: str, expense_type_id: int) -> ExpenseType:
        expense_type = self.expense_type.query.filter(self.expense_type.title == title,
                                                      self.expense_type.id != expense_type_id).first()
        return expense_type
