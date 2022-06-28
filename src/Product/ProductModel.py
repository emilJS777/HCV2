from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Product(Model, db.Model):
    name = db.Column(db.String(60))
    code = db.Column(db.String(10))
    description = db.Column(db.String(120))
    wholesale_price = db.Column(db.Numeric(8, 2))
    retail_price = db.Column(db.Numeric(8, 2))
    count = db.Column(db.Numeric(15, 1))

    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'))
    product_type = relationship("ProductType")

    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))
    unit = relationship("Unit")

    storage_id = db.Column(db.Integer, db.ForeignKey('storage.id'))
    storage = relationship("Storage")

    client_id = db.Column(db.Integer)
