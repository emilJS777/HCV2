from sqlalchemy import or_
from src.__Parents.Repository import Repository
from .IProductRepo import IProductRepo
from .ProductModel import Product
from flask import g

from ..Storage.StorageModel import Storage


class ProductRepository(Repository, IProductRepo):
    product: Product = Product

    def create(self, body: dict, client_id: int):
        product = self.product()
        product.name = body['name']
        product.description = body['description']

        product.product_type_id = body['product_type_id']
        product.storage_id = body['storage_id']
        product.code = body['code']
        product.wholesale_price = body['wholesale_price']
        product.retail_price = body['retail_price']
        product.count = body['count']
        product.unit_id = body['unit_id']
        product.client_id = client_id
        product.save_db()

    def update(self, product: Product, body: dict):
        product.name = body['name']
        product.description = body['description']
        product.product_type_id = body['product_type_id']
        product.storage_id = body['storage_id']
        product.code = body['code']
        product.wholesale_price = body['wholesale_price']
        product.retail_price = body['retail_price']
        product.count = body['count']
        product.unit_id = body['unit_id']
        product.update_db()

    def delete(self, product: Product):
        product.delete_db()

    def get_by_id(self, product_id: int, client_id: int) -> Product:
        product = self.product.query.filter_by(id=product_id, client_id=client_id).join(self.product.storage)\
            .filter(Storage.firm_id.in_(g.allowed_firm_ids)).first()
        return product

    def get_all(self, page: int, per_page: int, product_type_id: int or None, storage_id: int or None, code: int or None, client_id: int) -> dict:
        products = self.product.query\
            .filter_by(client_id=client_id)\
            .filter(self.product.product_type_id == product_type_id if product_type_id else self.product.product_type_id.isnot(None),
                    self.product.storage_id == storage_id if storage_id else self.product.storage_id.isnot(None),
                    self.product.code == code if code else self.product.code.isnot(None))\
            .join(self.product.storage)\
            .filter(Storage.firm_id.in_(g.allowed_firm_ids))\
            .paginate(page=page, per_page=per_page)

        for product in products.items:
            product.unit = product.unit
        return self.get_page_items(products)

