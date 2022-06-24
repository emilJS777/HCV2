from src.__Parents.Service import Service
from .IProductRepo import IProductRepo
from flask import g
from ..__Parents.Repository import Repository


class ProductService(Service, Repository):
    def __init__(self, product_repository: IProductRepo):
        self.product_repository: IProductRepo = product_repository

    # CREATE
    def create(self, body: dict) -> dict:
        self.product_repository.create(
            body=body,
            client_id=g.client_id)

        return self.response_created('продукт создан')

    # UPDATE
    def update(self, product_id: int, body: dict) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        self.product_repository.update(product=product, body=body)
        return self.response_updated('продукт обновлен')

    # DELETE
    def delete(self, product_id: int) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        self.product_repository.delete(product=product)
        return self.response_deleted('продукт удален')

    # GET BY ID
    def get_by_id(self, product_id: int) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        return self.response_ok(self.get_dict_items(product))

    # GET ALL
    def get_all(self, page: int, per_page: int, product_type_id: int or None, firm_id: int) -> dict:
        products = self.product_repository.get_all(
            page=page,
            per_page=per_page,
            product_type_id=product_type_id,
            firm_id=firm_id,
            client_id=g.client_id)

        return self.response_ok(products)
