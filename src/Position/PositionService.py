from .IPositionRepo import IPositionRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class PositionService(Service, Repository):
    def __init__(self, position_repository: IPositionRepo):
        self.position_repository: IPositionRepo = position_repository

    def create(self, body: dict) -> dict:
        if self.position_repository.get_by_title(title=body['title']):
            return self.response_conflict('такая позиция существует в системе')

        self.position_repository.create(body=body)
        return self.response_created('позиция успешно создана')

    def update(self, body: dict, position_id: int) -> dict:
        position = self.position_repository.get_by_id(position_id)
        if not position:
            return self.response_not_found('позиция не найдена')

        self.position_repository.update(position=position, body=body)
        return self.response_updated('позиция успешно обновлена')

    def delete(self, position_id: int) -> dict:
        position = self.position_repository.get_by_id(position_id)
        if not position:
            return self.response_not_found('позиция не найдена')

        self.position_repository.delete(position)
        return self.response_deleted('позиция удалена')

    def get_by_id(self, position_id: int) -> dict:
        position = self.position_repository.get_by_id(position_id)
        if not position:
            return self.response_not_found('позиция не найдена')

        return self.response_ok(self.get_dict_items(position))

    def get_all(self) -> dict:
        positions = self.position_repository.get_all()
        return self.response_ok(positions)
