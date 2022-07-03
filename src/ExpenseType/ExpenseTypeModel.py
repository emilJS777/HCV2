from src import db
from src.__Parents.Model import Model


class ExpenseType(Model, db.Model):
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(80))
