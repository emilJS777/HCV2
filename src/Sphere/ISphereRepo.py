from abc import ABC, abstractmethod
from src.Sphere.SphereModel import Sphere


class ISphereRepo(ABC):

    @abstractmethod
    def create(self, body: dict):
        pass

    @abstractmethod
    def update(self, sphere: Sphere, body: dict):
        pass

    @abstractmethod
    def delete(self, sphere: Sphere):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, sphere_id: int):
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Sphere:
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, sphere_id: int, name: str) -> Sphere:
        pass
