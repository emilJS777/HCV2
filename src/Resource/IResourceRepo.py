from abc import ABC, abstractmethod
from .ResourceModel import Resource


class IResourceRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, resource: Resource, body: dict):
        pass

    @abstractmethod
    def delete(self, resource: Resource):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, resource_id: int) -> Resource:
        pass
