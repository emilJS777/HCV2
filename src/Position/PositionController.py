from src.__Parents.Controller import Controller
from .PositionService import PositionService
from .PositionRepository import PositionRepository
from flask_expects_json import expects_json
from .PositionValidator import position_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class PositionController(Controller):
    position_service: PositionService = PositionService(PositionRepository())

    @expects_json(position_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('position_edit')
    def post(self) -> dict:
        res: dict = self.position_service.create(body=self.request.get_json())
        return res

    @expects_json(position_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('position_edit')
    def put(self) -> dict:
        res: dict = self.position_service.update(position_id=self.id, body=self.request.get_json())
        return res

    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('position_edit')
    def delete(self) -> dict:
        res: dict = self.position_service.delete(position_id=self.id)
        return res

    def get(self) -> dict:
        if self.id:
            res: dict = self.position_service.get_by_id(position_id=self.id)
        else:
            res: dict = self.position_service.get_all()
        return res

