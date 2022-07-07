from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Employee(Model, db.Model):
    title = db.Column(db.String(60), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    position = db.Column(db.String(60), nullable=False)

    adoption_date = db.Column(db.Date())
    birth_date = db.Column(db.Date())

    employee_bank_account = db.Column(db.String(60))
    social_card = db.Column(db.String(60))

    passport_number = db.Column(db.String(60))
    phone_number = db.Column(db.String(60))

    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))
    firm = relationship("Firm")

    client_id = db.Column(db.Integer, nullable=False)
