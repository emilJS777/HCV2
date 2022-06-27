from functools import wraps
from flask import g, request
from src.Permission.PermissionRepository import PermissionRepository
from src.__Parents.Service import Service


class PermissionMiddleware(Service):
    permission_repository = PermissionRepository()

    @staticmethod
    def check_permission(permission_name):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):

                for permission in g.user.permissions:
                    if permission.name == permission_name:
                        return f(*args, **kwargs)

                return PermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
