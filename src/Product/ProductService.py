from src.__Parents.Service import Service
from .IProductRepo import IProductRepo
from flask import g
from ..ProductType.IProductTypeRepo import IProductTypeRepo
from ..Storage.IStorageRepo import IStorageRepo
from ..__Parents.Repository import Repository


class ProductService(Service, Repository):
    def __init__(self, product_repository: IProductRepo, product_type_repository: IProductTypeRepo, storage_repository: IStorageRepo):
        self.product_repository: IProductRepo = product_repository
        self.product_type_repository: IProductTypeRepo = product_type_repository
        self.storage_repository: IStorageRepo = storage_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if not self.product_type_repository.get_by_id(product_type_id=body['product_type_id'], client_id=g.client_id):
            return self.response_not_found('тип продукта не найден')

        if not self.storage_repository.get_by_id(body['storage_id']):
            return self.response_not_found('хранилище не найдено')

        self.product_repository.create(
            body=body,
            client_id=g.client_id)

        return self.response_created('продукт создан')

    # UPDATE
    def update(self, product_id: int, body: dict) -> dict:
        product = self.product_repository.get_by_id(product_id=product_id, client_id=g.client_id)
        if not product:
            return self.response_not_found('продукт не найден')

        if not self.product_type_repository.get_by_id(product_type_id=body['product_type_id'], client_id=g.client_id):
            return self.response_not_found('тип продукта не найден ')

        if not self.storage_repository.get_by_id(body['storage_id']):
            return self.response_not_found('хранилище не найдено')

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

        return self.response_ok({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "product_type": {'title': product.product_type.title},
            "storage": {'title': product.storage.title}
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, product_type_id: int or None, storage_id: int or None) -> dict:
        products = self.product_repository.get_all(
            page=page,
            per_page=per_page,
            product_type_id=product_type_id,
            storage_id=storage_id,
            client_id=g.client_id)

        return self.response_ok(products)
