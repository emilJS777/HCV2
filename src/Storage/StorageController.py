from .StorageRepository import StorageRepository
from .StorageService import StorageService
from src.__Parents.Controller import Controller
from flask_expects_json import expects_json
from .StorageValidator import storage_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.FirmPermission.FirmPermissionMiddleware import FirmPermissionMiddleware
from src.Firm.FirmRepository import FirmRepository


class StorageController(Controller):
    storage_service: StorageService = StorageService(StorageRepository(), FirmRepository())

    # POST
    @expects_json(storage_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('storage_edit', firm_request=True)
    def post(self) -> dict:
        res: dict = self.storage_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(storage_schema)
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('storage_edit', firm_request=True)
    def put(self) -> dict:
        res: dict = self.storage_service.update(storage_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('storage_edit')
    def delete(self) -> dict:
        res: dict = self.storage_service.delete(storage_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @FirmPermissionMiddleware.check_permission('storage_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.storage_service.get_by_id(storage_id=self.id)
        else:
            res: dict = self.storage_service.get_all(
                page=self.page,
                per_page=self.per_page,
                firm_id=self.arguments.get('firm_id'),
                code=self.arguments.get('code'))
        return res
