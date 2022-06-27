from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class UserFirmPermission(Model, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    firm_permission_id = db.Column(db.Integer, db.ForeignKey("firm_permission.id"))


class FirmPermission(Model, db.Model):
    name = db.Column(db.String(60))
    title = db.Column(db.String(60))
    firm_id = db.Column(db.Integer, nullable=False)

    users = relationship("User", secondary="user_firm_permission", backref=db.backref('firm_permission'))
    client_id = db.Column(db.Integer, nullable=False)
