from src import db
from src.__Parents.Model import Model


class Sphere(Model, db.Model):
    name = db.Column(db.String(40), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)

