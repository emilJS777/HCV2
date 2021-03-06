from .IAuthModel import IAuthModel
from src.User.IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask_jwt_extended import get_jwt_identity
from flask import request, g


class AuthService(Service, Repository):
    def __init__(self, auth_repository: IAuthModel, user_repository: IUserRepo):
        self.__auth_repository = auth_repository
        self.__user_repository = user_repository

    def login(self, body: dict) -> dict:
        user = self.__user_repository.get_by_name(name=body['name'])

        if not user or not check_password_hash(user.password_hash, body['password']):
            return self.response_invalid_login()

        auth = self.__auth_repository.generate_tokens(user.id)
        return self.response_ok(auth)

    def refresh(self) -> dict:

        auth = self.__auth_repository.get_by_user_id(user_id=get_jwt_identity())
        if auth['refresh_token'] == request.headers['authorization'].split(' ')[1]:

            auth = self.__auth_repository.generate_tokens(get_jwt_identity())
            self.response_ok(auth)

        return self.response_invalid_login()

    def get_profile(self) -> dict:
        return self.response_ok({
            'id': g.user.id,
            'first_name': g.user.first_name,
            'last_name': g.user.last_name,
            'email_address': g.user.email_address,
            'image_path': g.user.image_path,
            'ticket': g.user.ticket,
            'position': self.get_dict_items(g.user.position),
            'client_id': g.user.client_id,
            'permissions': self.get_array_items(g.user.permissions),
            'firm_permissions': self.get_array_items(g.user.firm_permissions)
        })
