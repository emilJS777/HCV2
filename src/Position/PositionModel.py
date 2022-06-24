from src import db
from src.__Parents.Model import Model


class Position(Model, db.Model):
    title = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(120))
