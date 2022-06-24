from src.__Parents.Repository import Repository
from .PositionModel import Position
from .IPositionRepo import IPositionRepo


class PositionRepository(Repository, IPositionRepo):
    position: Position = Position

    def create(self, body: dict) -> Position:
        position = Position()
        position.title = body['title']
        position.description = body['description']
        position.save_db()
        return position

    def update(self, position: Position, body: dict) -> Position:
        position.title = body['title']
        position.description = body['description']
        position.update_db()
        return position

    def delete(self, position: Position) -> dict:
        position.delete_db()
        return position

    def get_all(self) -> list[dict]:
        positions = self.position.query.all()
        return self.get_array_items(positions)

    def get_by_id(self, position_id: int) -> Position:
        position = self.position.query.filter_by(id=position_id).first()
        return position

    def get_by_title(self, title: str) -> Position:
        position = self.position.query.filter_by(title=title).first()
        return position
