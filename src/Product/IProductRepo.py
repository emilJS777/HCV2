from abc import ABC, abstractmethod
from .ProductModel import Product


class IProductRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int):
        pass

    @abstractmethod
    def update(self, product: Product, body: dict):
        pass

    @abstractmethod
    def delete(self, product: Product):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, product_type_id: int or None, storage_id: int or None, code: int or None, client_id: int) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int, client_id: int) -> Product:
        pass
