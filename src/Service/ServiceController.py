from src.__Parents.Controller import Controller
from .ServiceService import ServiceService
from .ServiceRepository import ServiceRepository
from src.Unit.UnitRepository import UnitRepository
from flask_expects_json import expects_json
from .ServiceValidator import service_schema
from src.Auth.AuthMiddleware import AuthMiddleware


class ServiceController(Controller):
    service_service: ServiceService = ServiceService(ServiceRepository(), UnitRepository())

    # POST
    @expects_json(service_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.service_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(service_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.service_service.update(
            service_id=self.id,
            body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.service_service.delete(service_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.service_service.get_by_id(self.id)
        else:
            res: dict = self.service_service.get_all(
                page=self.page,
                per_page=self.per_page,
                search=self.arguments.get('search'))
        return res
