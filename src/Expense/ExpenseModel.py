from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Expense(Model, db.Model):
    title = db.Column(db.String(60))
    description = db.Column(db.String(120))

    price = db.Column(db.Numeric(8, 2))
    count = db.Column(db.Numeric(8, 2))

    colleague_id = db.Column(db.Integer, db.ForeignKey("colleague.id"))
    colleague = relationship("Colleague")

    expense_type_id = db.Column(db.Integer, db.ForeignKey("expense_type.id"))
    expense_type = relationship("ExpenseType")

    firm_id = db.Column(db.Integer, db.ForeignKey("firm.id"))
    firm = relationship("Firm")

    creation_date = db.Column(db.Date, default=datetime.utcnow())
    client_id = db.Column(db.Integer)

