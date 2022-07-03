from src import db
from src.__Parents.Model import Model


class Colleague(Model, db.Model):
    title = db.Column(db.String(40), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    activity_address = db.Column(db.String(60), nullable=False)
    legal_address = db.Column(db.String(60), nullable=False)

    phone_number = db.Column(db.Integer, nullable=False)
    hvhh = db.Column(db.String(60))

    client_id = db.Column(db.Integer)
