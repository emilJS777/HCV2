from src.__Parents.Controller import Controller
from .UserService import UserService
from .UserRepository import UserRepository
from src.Permission.PermissionMiddleware import PermissionMiddleware
from flask_expects_json import expects_json
from .UserValidator import user_create_schema, user_registration_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from ..Permission.PermissionRepository import PermissionRepository
from src.Position.PositionRepository import PositionRepository


class UserController(Controller):
    user_service = UserService(UserRepository(), PermissionRepository(), PositionRepository())

    @expects_json(user_create_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('user_edit')
    def post(self):
        return self.user_service.create(
            body=self.request.get_json()
        )

    @expects_json(user_create_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('user_edit')
    def put(self):
        return self.user_service.update(
            user_id=self.id,
            body=self.request.get_json()
        )

    @expects_json(user_registration_schema)
    def patch(self):
        return self.user_service.registration(
            body=self.request.get_json()
        )

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('user_edit')
    def delete(self):
        return self.user_service.delete(
            user_id=self.id
        )

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('user_get')
    def get(self):
        if self.id:
            return self.user_service.get_by_id(self.id)

        else:
            return self.user_service.get_all(
                page=self.page,
                per_page=self.per_page,
                position_id=self.arguments.get('position_id')
            )

