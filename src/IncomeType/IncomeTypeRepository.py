from .IIncomeTypeRepo import IIncomeTypeRepo
from src.__Parents.Repository import Repository
from .IncomeTypeModel import IncomeType


class IncomeTypeRepository(Repository, IIncomeTypeRepo):
    income_type: IncomeType = IncomeType

    def create(self, body: dict):
        income_type = self.income_type()
        income_type.title = body['title']
        income_type.description = body['description']
        income_type.save_db()

    def update(self, income_type: IncomeType, body: dict):
        income_type.title = body['title']
        income_type.description = body['description']
        income_type.update_db()

    def delete(self, income_type: IncomeType):
        income_type.delete_db()

    def get_by_id(self, income_type_id: int) -> IncomeType:
        income_type = self.income_type.query.filter_by(id=income_type_id).first()
        return income_type

    def get_by_title(self, title: str) -> IncomeType:
        income_type = self.income_type.query.filter_by(title=title).first()
        return income_type

    def get_all(self):
        income_types = self.income_type.query.all()
        return self.get_array_items(income_types)

    def get_by_title_exclude_id(self, title: str, income_type_id: int) -> IncomeType:
        income_type = self.income_type.query.filter(self.income_type.title == title,
                                                    self.income_type.id != income_type_id).first()
        return income_type
