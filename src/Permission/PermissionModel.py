from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class UserPermission(Model, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    permission_id = db.Column(db.Integer, db.ForeignKey("permission.id"))


class Permission(Model, db.Model):
    name = db.Column(db.String(60), unique=True)
    title = db.Column(db.String(60), unique=True)

    users = relationship("User", secondary="user_permission", backref=db.backref('permission'))
