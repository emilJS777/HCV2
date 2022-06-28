from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Product(Model, db.Model):
    name = db.Column(db.String(60))
    description = db.Column(db.String(120))

    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    product_type = relationship("ProductType")

    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    storage = relationship("Storage")

    client_id = db.Column(db.Integer)
