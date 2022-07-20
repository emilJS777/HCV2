from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model
from datetime import datetime


class Income(Model, db.Model):

    price = db.Column(db.Numeric(8, 2))
    count = db.Column(db.Numeric(8, 2))

    colleague_id = db.Column(db.Integer, db.ForeignKey("colleague.id"))
    colleague = relationship("Colleague")

    income_type_id = db.Column(db.Integer, db.ForeignKey("income_type.id"))
    income_type = relationship("IncomeType")

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    product = relationship("Product")

    firm_id = db.Column(db.Integer, db.ForeignKey("firm.id"))
    firm = relationship("Firm")

    creation_date = db.Column(db.Date, default=datetime.utcnow())
    client_id = db.Column(db.Integer)

