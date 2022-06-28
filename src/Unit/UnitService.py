from .IUnitRepo import IUnitRepo
from src.__Parents.Service import Service


class UnitService(Service):
    def __init__(self, unit_repository: IUnitRepo):
        self.unit_repository: IUnitRepo = unit_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.unit_repository.get_by_title(body['title']):
            return self.response_conflict('единица измерения уже существует')

        self.unit_repository.create(body)
        return self.response_created('единица измерения создана')

    # UPDATE
    def update(self, unit_id: int, body: dict) -> dict:
        unit = self.unit_repository.get_by_id(unit_id)
        if not unit:
            return self.response_not_found('единица измерения не найдена')

        self.unit_repository.update(unit=unit, body=body)
        return self.response_updated('единица измерения обновлена')

    # DELETE
    def delete(self, unit_id: int) -> dict:
        unit = self.unit_repository.get_by_id(unit_id)
        if not unit:
            return self.response_not_found('единица измерения не найдена')

        self.unit_repository.delete(unit=unit)
        return self.response_deleted('единица измерения удалена')

    # GET BY ID
    def get_by_id(self, unit_id: int) -> dict:
        unit = self.unit_repository.get_by_id(unit_id)
        if not unit:
            return self.response_not_found('единица измерения не найдена')

        return self.response_ok({"id": unit.id, "title": unit.title, "description": unit.description})

    # GET ALL
    def get_all(self) -> dict:
        units = self.unit_repository.get_all()
        return self.response_ok(units)
    