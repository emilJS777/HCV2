from src.__Parents.Repository import Repository
from .IProductTypeRepo import IProductTypeRepo
from .ProductTypeModel import ProductType


class ProductTypeRepository(Repository, IProductTypeRepo):
    product_type: ProductType = ProductType

    def create(self, body: dict, client_id: int):
        product_type = self.product_type()
        product_type.title = body['title']
        product_type.description = body['description']
        product_type.client_id = client_id
        product_type.save_db()

    def update(self, product_type: ProductType, body: dict):
        product_type.title = body['title']
        product_type.description = body['description']
        product_type.update_db()

    def delete(self, product_type: ProductType):
        product_type.delete_db()

    def get_all(self, client_id: int):
        product_types = self.product_type.query.filter_by(client_id=client_id).all()
        return self.get_array_items(product_types)

    def get_by_id(self, product_type_id: int,  client_id: int):
        product_type = self.product_type.query.filter_by(id=product_type_id, client_id=client_id).first()
        return product_type

    def get_by_title(self, title: str,  client_id: int) -> ProductType:
        product_type = self.product_type.query.filter_by(title=title).first()
        return product_type

    def get_by_title_exclude_id(self, product_type_id: int, title: str,  client_id: int) -> ProductType:
        product_type = self.product_type.query.filter(self.product_type.title == title,
                                                      self.product_type.id != product_type_id,
                                                      self.product_type.client_id == client_id).first()
        return product_type
