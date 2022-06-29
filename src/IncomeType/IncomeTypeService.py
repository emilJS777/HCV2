from .IIncomeTypeRepo import IIncomeTypeRepo
from ..__Parents.Service import Service


class IncomeTypeService(Service):
    def __init__(self, income_type_repository: IIncomeTypeRepo):
        self.income_type_repository: IIncomeTypeRepo = income_type_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.income_type_repository.get_by_title(body['title']):
            return self.response_conflict('тип прибыли уже существует')

        self.income_type_repository.create(body)
        return self.response_created('тип прибыли создан')

    # UPDATE
    def update(self, income_type_id: int, body: dict) -> dict:
        income_type = self.income_type_repository.get_by_id(income_type_id)

        if not income_type:
            return self.response_not_found('тип прибыли не найден')

        if self.income_type_repository.get_by_title_exclude_id(title=body['title'], income_type_id=income_type_id):
            return self.response_conflict('тип прибыли по такому названию уже существует')

        self.income_type_repository.update(income_type=income_type, body=body)
        return self.response_updated('тип прибыли обновлен')

    # DELETE
    def delete(self, income_type_id: int) -> dict:
        income_type = self.income_type_repository.get_by_id(income_type_id)
        if not income_type:
            return self.response_not_found('тип прибыли не найден')

        self.income_type_repository.delete(income_type)
        return self.response_deleted('тип прибыли удален')

    # GET BY ID
    def get_by_id(self, income_type_id: int) -> dict:
        income_type = self.income_type_repository.get_by_id(income_type_id)
        if not income_type:
            return self.response_not_found('тип прибыли не найден')

        return self.response_ok({'id': income_type.id,
                                 'title': income_type.title,
                                 'description': income_type.description})

    # GET ALL
    def get_all(self) -> dict:
        income_types = self.income_type_repository.get_all()
        return self.response_ok(income_types)
