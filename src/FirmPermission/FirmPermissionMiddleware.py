from functools import wraps
from flask import g, request
from src.FirmPermission.FirmPermissionRepository import FirmPermissionRepository
from src.__Parents.Service import Service


class FirmPermissionMiddleware(Service):
    firm_permission_repository = FirmPermissionRepository()

    @staticmethod
    def check_permission(permission_name):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):

                for firm_permission in g.user.firm_permissions:
                    if firm_permission.name == permission_name and firm_permission.firm_id == int(request.args.get('firm_id') or request.get_json()['firm_id']):
                        return f(*args, **kwargs)

                return FirmPermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
