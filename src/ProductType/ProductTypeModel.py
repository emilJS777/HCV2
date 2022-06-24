from src import db
from src.__Parents.Model import Model


class ProductType(Model, db.Model):
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(60))

    client_id = db.Column(db.Integer, nullable=False)
