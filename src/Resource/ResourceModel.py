from src import db
from src.__Parents.Model import Model


class Resource(Model, db.Model):
    title = db.Column(db.String(60))

    input_date = db.Column(db.Date())
    operation_date = db.Column(db.Date())

    hm_type = db.Column(db.String(80))
    hm_group = db.Column(db.String(80))

    employee_bank_account = db.Column(db.String(80))
    location = db.Column(db.String(80))

    client_id = db.Column(db.Integer)
