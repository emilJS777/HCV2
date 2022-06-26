from sqlalchemy.orm import joinedload

from src.__Parents.Repository import Repository
from .IUserRepo import IUserRepo
from .UserModel import User
from flask_bcrypt import generate_password_hash


class UserRepository(Repository, IUserRepo):
    user: User = User

    def create(self, body: dict, client_id: int, permissions: list) -> dict:
        user = self.user()
        user.ticket = body['ticket']
        user.first_name = body['first_name'].title()
        user.last_name = body['last_name'].title()
        user.email_address = body['email_address']
        user.position_id = body['position_id']
        user.client_id = client_id
        user.permissions = permissions
        user.save_db()
        return user

    def update(self, user_id: int, body: dict, client_id: int, permissions: list) -> dict:
        user = self.user.query.filter_by(id=user_id, client_id=client_id).first()
        user.first_name = body['first_name']
        user.last_name = body['last_name']
        user.email_address = body['email_address'],
        user.position_id = body['position_id']
        user.permissions = permissions
        user.update_db()
        return user

    def update_auth(self, user_id: int, body: dict) -> dict:
        user = self.user.query.filter_by(id=user_id).first()

        if body.get('password'):
            user.password_hash = generate_password_hash(body['password'])

        if body.get('name'):
            user.name = body['name']

        user.ticket = None
        user.update_db()
        return user

    def delete(self, user_id: int, client_id: int) -> dict:
        user = self.user.query.filter_by(id=user_id, client_id=client_id).first()
        user.delete_db()
        return user

    def get_by_id(self, user_id: int, client_id: int or None) -> User:
        user = self.user.query.filter(self.user.id == user_id,
                                      self.user.client_id == client_id
                                      if client_id else
                                      self.user.client_id.isnot(None)).first()
        return user

    def get_by_name(self, name: str) -> dict:
        user = self.user.query.filter_by(name=name).first()
        return user

    def get_by_name_exclude_id(self, user_id: int, name: str, client_id: int) -> dict:
        user = self.user.query.filter(self.user.id != user_id,
                                      self.user.name == name,
                                      self.user.client_id == client_id).first()
        return self.get_dict_items(user)

    def get_all(self, page: int, per_page: int, position_id: int or None, client_id: int) -> dict:
        users = self.user.query.filter_by(client_id=client_id)\
            .filter(User.position_id == position_id if position_id else User.position_id.isnot(None))\
            .paginate(page=page, per_page=per_page)
        for user in users.items:
            user.position = user.position
        return self.get_page_items(users)

    def get_by_ticket(self, ticket: str) -> User:
        user = self.user.query.filter_by(ticket=ticket).first()
        return user

    def get_by_first_client_id(self, client_id: int) -> User:
        user = self.user.query.filter_by(client_id=client_id).first()
        return user

    def get_permissions_by_user_id(self, user_id: int, permission_ids: list or None = None):
        user = self.user.query.filter_by(id=user_id).first()

        if permission_ids:
            found_permissions: list = []

            for permission in user.permissions:
                if permission.id in permission_ids:
                    found_permissions.append(permission)

            return found_permissions
        else:
            return user.permissions

    def get_by_email_address(self, email_address: str) -> User:
        user = self.user.query.filter_by(email_address=email_address).first()
        return user

    def get_by_email_address_exclude_id(self, user_id: int, email_address: str) -> User:
        user = self.user.query.filter(self.user.email_address == email_address, self.user.id != user_id).first()
        return user

