from .SphereService import SphereService
from .SpeheRepository import SphereRepository
from ..Auth.AuthMiddleware import AuthMiddleware
from ..__Parents.Controller import Controller
from src.Permission.PermissionMiddleware import PermissionMiddleware
from flask_expects_json import expects_json
from .SphereValidator import sphere_schema


class SphereController(Controller):
    sphere_service = SphereService(SphereRepository())

    @expects_json(sphere_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('sphere_edit')
    def post(self) -> dict:
        res: dict = self.sphere_service.create(body=self.request.get_json())
        return res

    @expects_json(sphere_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('sphere_edit')
    def put(self) -> dict:
        res: dict = self.sphere_service.update(body=self.request.get_json(), sphere_id=self.id)
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('sphere_edit')
    def delete(self) -> dict:
        res: dict = self.sphere_service.delete(sphere_id=self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.sphere_service.get_by_id(sphere_id=self.id)
        else:
            res: dict = self.sphere_service.get_all()
        return res
