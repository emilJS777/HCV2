from sqlalchemy import or_
from src.__Parents.Repository import Repository
from .IProductRepo import IProductRepo
from .ProductModel import Product


class ProductRepository(Repository, IProductRepo):
    product: Product = Product

    def create(self, body: dict, client_id: int):
        product = self.product()
        product.name = body['name']
        product.description = body['description']

        product.product_type_id = body['product_type_id']
        product.firm_id = body['firm_id']
        product.client_id = client_id
        product.save_db()

    def update(self, product: Product, body: dict):
        product.name = body['name']
        product.description = body['description']
        product.product_type_id = body['product_type_id']
        product.firm_id = body['firm_id']
        product.update_db()

    def delete(self, product: Product):
        product.delete_db()

    def get_by_id(self, product_id: int, client_id: int) -> Product:
        product = self.product.query.filter_by(id=product_id, client_id=client_id).first()
        return product

    def get_all(self, page: int, per_page: int, product_type_id: int or None, firm_id: int, client_id: int) -> list[dict]:
        products = self.product.query.filter_by(client_id=client_id, firm_id=firm_id)\
            .filter(or_(self.product.product_type_id == product_type_id, self.product.product_type_id.isnot(None)))\
            .paginate(page=page, per_page=per_page)
        return self.get_page_items(products)

