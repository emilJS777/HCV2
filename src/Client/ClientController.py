from src.__Parents.Controller import Controller
from .ClientService import ClientService
from .ClientRepository import ClientRepository
from flask_expects_json import expects_json
from src.Auth.AuthMiddleware import AuthMiddleware
from .ClientValidator import client_schema


class ClientController(Controller):
    client_service = ClientService(ClientRepository())

    # CREATE
    @expects_json(client_schema)
    @AuthMiddleware.check_authorize
    def post(self) -> dict:
        res: dict = self.client_service.create(body=self.request.get_json())
        return res

    # UPDATE
    @expects_json(client_schema)
    @AuthMiddleware.check_authorize
    def put(self) -> dict:
        res: dict = self.client_service.update(
            client_id=self.id,
            body=self.request.get_json()
        )
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    def delete(self) -> dict:
        res: dict = self.client_service.delete(
            client_id=self.id
        )
        return res

    # GET
    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.client_service.get_by_id(client_id=self.id)
        else:
            res: dict = self.client_service.get_all(page=self.page, per_page=self.per_page)

        return res
