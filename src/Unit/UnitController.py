from .UnitService import UnitService
from src.__Parents.Controller import Controller
from .UnitRepository import UnitRepository
from flask_expects_json import expects_json
from .UnitValidator import unit_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class UnitController(Controller):
    unit_service: UnitService = UnitService(UnitRepository())

    # POST
    @expects_json(unit_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('unit_edit')
    def post(self) -> dict:
        res: dict = self.unit_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(unit_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('unit_edit')
    def put(self) -> dict:
        res: dict = self.unit_service.update(unit_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('unit_edit')
    def delete(self) -> dict:
        res: dict = self.unit_service.delete(unit_id=self.id)
        return res

    # GET
    def get(self) -> dict:
        if self.id:
            res: dict = self.unit_service.get_by_id(self.id)
        else:
            res: dict = self.unit_service.get_all()
        return res
