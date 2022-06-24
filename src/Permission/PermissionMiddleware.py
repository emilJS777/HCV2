from functools import wraps
from flask import g
from src.Permission.PermissionRepository import PermissionRepository
from src.__Parents.Service import Service


class PermissionMiddleware(Service):
    permission_repository = PermissionRepository()

    @staticmethod
    def check_permission(permission_name):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                if PermissionMiddleware.permission_repository.get_by_name_user_id(permission_name, g.user_id):
                    return f(*args, **kwargs)

                return PermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
