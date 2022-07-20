from src.__Parents.Controller import Controller
from .FirmRepository import FirmRepository
from .FirmService import FirmService
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware
from flask_expects_json import expects_json
from .FirmValidator import firm_schema
from src.FirmPermission.FirmPermissionRepository import FirmPermissionRepository
from ..Sphere.SpeheRepository import SphereRepository
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware


class FirmController(Controller):
    firm_service: FirmService = FirmService(FirmRepository(), FirmPermissionRepository(), SphereRepository())

    @expects_json(firm_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('firm_edit')
    def post(self) -> dict:
        res: dict = self.firm_service.create(body=self.request.get_json())
        return res

    @expects_json(firm_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('firm_edit')
    def put(self) -> dict:
        res: dict = self.firm_service.update(
            body=self.request.get_json(),
            firm_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('firm_edit')
    def delete(self) -> dict:
        res: dict = self.firm_service.delete(firm_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission(False)
    def get(self) -> dict:
        if self.id:
            res: dict = self.firm_service.get_by_id(self.id)
        else:
            res: dict = self.firm_service.get_all(page=self.page,
                                                  per_page=self.per_page,
                                                  title=self.arguments.get('title'),
                                                  sphere_id=self.arguments.get('sphere_id'))

        return res
