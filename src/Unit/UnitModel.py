from src import db
from src.__Parents.Model import Model


class Unit(Model, db.Model):
    title = db.Column(db.String(40), nullable=False, unique=True)
    description = db.Column(db.String(80))
