from sqlalchemy.orm import relationship
from src import db
from src.__Parents.Model import Model


class User(Model, db.Model):
    name = db.Column(db.String(60), unique=True)
    first_name = db.Column(db.String(24), nullable=False)
    last_name = db.Column(db.String(24), nullable=False)
    email_address = db.Column(db.String(60), nullable=False)
    image_path = db.Column(db.String(120))
    ticket = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(200))

    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    position = relationship("Position")
    permissions = relationship("Permission", secondary="user_permission", backref=db.backref('user'))
    client_id = db.Column(db.Integer)
