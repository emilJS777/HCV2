from src.__Parents.Controller import Controller
from .ResourceService import ResourceService
from .ResourceRepository import ResourceRepository
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from flask_expects_json import expects_json
from .ResourceValidator import resource_schema
from src.Firm.FirmRepository import FirmRepository


class ResourceController(Controller):
    resource_service: ResourceService = ResourceService(ResourceRepository(), FirmRepository())

    # POST
    @expects_json(resource_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('resource_edit')
    def post(self) -> dict:
        res: dict = self.resource_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(resource_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('resource_edit')
    def put(self) -> dict:
        res: dict = self.resource_service.update(resource_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('resource_edit')
    def delete(self) -> dict:
        res: dict = self.resource_service.delete(self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('resource_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.resource_service.get_by_id(self.id)
        else:
            res: dict = self.resource_service.get_all(
                page=self.page,
                per_page=self.per_page,
                firm_id=self.arguments.get('firm_id'))
        return res
