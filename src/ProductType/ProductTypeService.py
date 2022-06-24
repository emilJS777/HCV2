from src.ProductType.IProductTypeRepo import IProductTypeRepo
from src.__Parents.Service import Service
from flask import g


class ProductTypeService(Service):
    def __init__(self, product_type_repository: IProductTypeRepo):
        self.product_type_repository: IProductTypeRepo = product_type_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.product_type_repository.get_by_title(title=body['title'], client_id=g.client_id):
            return self.response_conflict('тип продукта уже существует')

        self.product_type_repository.create(body, client_id=g.client_id)
        return self.response_created('тип продукта создан')

    # UPDATE
    def update(self, product_type_id: int, body: dict) -> dict:
        product_type = self.product_type_repository.get_by_id(product_type_id=product_type_id,
                                                              client_id=g.client_id)

        if not product_type:
            return self.response_not_found('тип продукта не найден')

        if self.product_type_repository.get_by_title_exclude_id(product_type_id=product_type_id,
                                                                title=body['title'],
                                                                client_id=g.client_id):
            return self.response_conflict('тип продукта уже существует')

        self.product_type_repository.update(product_type=product_type,
                                            body=body)
        return self.response_updated('тип продукта обновлен ')

    # DELETED
    def delete(self, product_type_id: int) -> dict:
        product_type = self.product_type_repository.get_by_id(product_type_id=product_type_id,
                                                              client_id=g.client_id)

        if not product_type:
            return self.response_not_found('тип продукта не найден')

        self.product_type_repository.delete(product_type)
        return self.response_deleted('тип продукта удален')

    # GET BY ID
    def get_by_id(self, product_type_id: int) -> dict:
        product_type = self.product_type_repository.get_by_id(product_type_id=product_type_id,
                                                              client_id=g.client_id)

        if not product_type:
            return self.response_not_found('тип продукта не найден')

        return self.response_ok(product_type)

    # GET ALL
    def get_all(self) -> dict:
        product_types = self.product_type_repository.get_all(client_id=g.client_id)
        return self.response_ok(product_types)
