from .IUserRepo import IUserRepo
from flask_bcrypt import check_password_hash
from ..Permission.IPermissionRepo import IPermissionRepo
from ..Position.IPositionRepo import IPositionRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class UserService(Service, Repository):
    def __init__(self,
                 user_repository: IUserRepo,
                 permission_repository: IPermissionRepo,
                 position_repository: IPositionRepo):

        self._user_repository: IUserRepo = user_repository
        self._permission_repository: IPermissionRepo = permission_repository
        self.position_repository: IPositionRepo = position_repository

    # FIND PERMISSION FROM G.USER.PERMISSION IN PERMISSION IDS
    @staticmethod
    def get_permissions_by_user_id(user_permissions: list, permission_ids: list) -> list:
        found_permissions: list = []
        for user_permission in user_permissions:
            if user_permission.id in permission_ids:
                found_permissions.append(user_permission)
        return found_permissions

    # CREATE
    def create(self, body: dict) -> dict:
        if self._user_repository.get_by_email_address(body['email_address']):
            return self.response_conflict('аддресс электронной почты существует в системе')

        if not self.position_repository.get_by_id(body['position_id']):
            return self.response_not_found('позиция не найдена')

        permissions: list = self.get_permissions_by_user_id(
            user_permissions=g.user.permissions,
            permission_ids=body['permission_ids'])

        firm_permissions: list = self.get_permissions_by_user_id(
            user_permissions=g.user.firm_permissions,
            permission_ids=body['firm_permission_ids'])

        body['ticket'] = self.generate_ticket_code()
        user = self._user_repository.create(
            body=body,
            client_id=g.client_id,
            permissions=permissions,
            firm_permissions=firm_permissions)

        return self.response_ok({'first_name': user.first_name,
                                 'last_name': user.last_name,
                                 'ticket': user.ticket,
                                 'position': user.position.title or None,
                                 'email_address': user.email_address,
                                 'id': user.id})

    # UPDATE
    def update(self, user_id: int, body: dict) -> dict:
        if not self._user_repository.get_by_id(user_id, client_id=g.client_id):
            return self.response_not_found('пользователь не найден')

        if not self.position_repository.get_by_id(body['position_id']):
            return self.response_not_found('позиция не найдена')

        if self._user_repository.get_by_email_address_exclude_id(user_id=user_id, email_address=body['email_address']):
            return self.response_conflict('аддресс электронной почты существует в системе')

        permissions: list = self.get_permissions_by_user_id(
            user_permissions=g.user.permissions,
            permission_ids=body['permission_ids'])

        firm_permissions: list = self.get_permissions_by_user_id(
            user_permissions=g.user.firm_permissions,
            permission_ids=body['firm_permission_ids'])

        self._user_repository.update(
            user_id=user_id,
            body=body,
            client_id=g.client_id,
            permissions=permissions,
            firm_permissions=firm_permissions)

        return self.response_updated('данные пользователя успешно обновлены')

    # REGISTRATION
    def registration(self, body: dict) -> dict:
        user = self._user_repository.get_by_ticket(ticket=body['ticket'])
        if not user:
            return self.response_not_found('тикет код не найден')

        if self._user_repository.get_by_name(name=body['name']):
            return self.response_conflict('пользователь с таким  именем существует')

        self._user_repository.update_auth(user_id=user.id, body=body)
        return self.response_updated('регстрация прошла успешно')

    # DELETE
    def delete(self, user_id: int):
        user = self._user_repository.get_by_id(user_id, client_id=g.client_id)

        if not user:
            return self.response_not_found('пользователь не найден')

        self._permission_repository.delete_user_permissions_by_user_id(user_id=user_id)
        self._user_repository.delete(user_id=user_id, client_id=g.client_id)
        return self.response_deleted('пользователь удален')

    # GET BY ID
    def get_by_id(self, user_id: int) -> dict:
        user = self._user_repository.get_by_id(user_id, client_id=g.client_id)
        if not user:
            return self.response_not_found('пользователь не найден')
        return self.response_ok({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email_address': user.email_address,
            'image_path': user.image_path,
            'ticket': user.ticket,
            'position': self.get_dict_items(user.position),
            'client_id': user.client_id,
            'permissions': self.get_array_items(user.permissions),
            'firm_permissions': self.get_array_items(user.firm_permissions)
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, position_id: int or None) -> dict:
        user_list: dict = self._user_repository.get_all(
            page=page,
            per_page=per_page,
            position_id=position_id,
            client_id=g.client_id)
        return self.response_ok(user_list)

