from abc import ABC, abstractmethod
from .PositionModel import Position


class IPositionRepo(ABC):

    @abstractmethod
    def create(self, body: dict) -> Position:
        pass

    @abstractmethod
    def update(self, position: Position, body: dict) -> Position:
        pass

    @abstractmethod
    def delete(self, position: Position) -> Position:
        pass

    @abstractmethod
    def get_all(self) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, position_id: int) -> Position:
        pass

    @abstractmethod
    def get_by_title(self, title: str) -> Position:
        pass
