from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Storage(Model, db.Model):
    title = db.Column(db.String(40), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(120))
    storekeeper = db.Column(db.String(80))
    address = db.Column(db.String(120))

    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))
    firm = relationship("Firm")

    client_id = db.Column(db.Integer, nullable=False)
