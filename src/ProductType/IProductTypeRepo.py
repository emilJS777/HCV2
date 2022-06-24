from abc import ABC, abstractmethod
from .ProductTypeModel import ProductType


class IProductTypeRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, product_type: ProductType, body: dict):
        pass

    @abstractmethod
    def delete(self, product_type: ProductType):
        pass

    @abstractmethod
    def get_all(self,  client_id: int):
        pass

    @abstractmethod
    def get_by_id(self, product_type_id: int, client_id: int):
        pass

    @abstractmethod
    def get_by_title(self, title: str, client_id: int) -> ProductType:
        pass

    @abstractmethod
    def get_by_title_exclude_id(self, product_type_id: int, title: str, client_id: int) -> ProductType:
        pass
