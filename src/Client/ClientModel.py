from src import db
from src.__Parents.Model import Model


class Client(Model, db.Model):
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

    parent_id = db.Column(db.Integer)
