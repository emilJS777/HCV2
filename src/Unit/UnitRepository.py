from .IUnitRepo import IUnitRepo
from src.__Parents.Repository import Repository
from .UnitModel import Unit


class UnitRepository(Repository, IUnitRepo):
    unit: Unit = Unit

    def create(self, body: dict):
        unit = self.unit()
        unit.title = body['title']
        unit.description = body['description']
        unit.save_db()

    def update(self, unit: Unit, body: dict):
        unit.title = body['title']
        unit.description = body['description']
        unit.update_db()

    def delete(self, unit: Unit):
        unit.delete_db()

    def get_by_id(self, unit_id: int) -> Unit:
        unit = self.unit.query.filter_by(id=unit_id).first()
        return unit

    def get_by_title(self, title: str) -> Unit:
        unit = self.unit.query.filter_by(title=title).first()
        return unit

    def get_all(self) -> dict:
        unit = self.unit.query.all()
        return self.get_array_items(unit)
