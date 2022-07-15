from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class Income(Model, db.Model):
    pass
    # income_type_id = db.Column(db.Integer, db.ForeignKey("income_type.id"))
    # income_type = relationship("income_type")
    #