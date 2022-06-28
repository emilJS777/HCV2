from functools import wraps
from flask import g, request
from src.FirmPermission.FirmPermissionRepository import FirmPermissionRepository
from src.__Parents.Service import Service


class FirmPermissionMiddleware(Service):
    firm_permission_repository = FirmPermissionRepository()

    @staticmethod
    def check_permission(permission_name: bool or str = False, firm_request: bool = False):

        def decoration(f):
            @wraps(f)
            def decoration_function(*args, **kwargs):
                allowed_firm_ids: list[int] = []

                for firm_permission in g.user.firm_permissions:
                    if permission_name:
                        if permission_name in firm_permission.name:
                            allowed_firm_ids.append(firm_permission.firm_id)
                    else:
                        allowed_firm_ids.append(firm_permission.firm_id)

                if firm_request:
                    firm_id: int = int(request.args.get('firm_id') or request.get_json()['firm_id'])
                    allowed = False
                    for firm_permission in g.user.firm_permissions:
                        if permission_name and firm_permission.name == permission_name and firm_permission.firm_id == firm_id:
                            allowed = True
                            break
                    if not allowed:
                        return FirmPermissionMiddleware.response_forbidden('ресурс запрещен')


                if len(allowed_firm_ids):
                    g.allowed_firm_ids = allowed_firm_ids
                    return f(*args, **kwargs)

                # for firm_permission in g.user.firm_permissions:
                #     if firm_permission.name == permission_name and firm_permission.firm_id == int(request.args.get('firm_id') or request.get_json()['firm_id']):
                #         return f(*args, **kwargs)

                return FirmPermissionMiddleware.response_forbidden('ресурс запрещен')
            return decoration_function
        return decoration
