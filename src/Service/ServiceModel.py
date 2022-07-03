from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Service(Model, db.Model):
    code = db.Column(db.String(10))
    title = db.Column(db.String(60))

    check = db.Column(db.String(60))
    wholesale_price = db.Column(db.Numeric(8, 2))
    retail_price = db.Column(db.Numeric(8, 2))

    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'))
    unit = relationship("Unit")

    client_id = db.Column(db.Integer)
