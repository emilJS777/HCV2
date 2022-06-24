from src.__Parents.Repository import Repository
from .IClientRepo import IClientRepo
from .ClientModel import Client


class ClientRepository(Repository, IClientRepo):
    client: Client = Client

    # CREATE
    def create(self, body: dict, parent_id: int or None) -> Client:
        client = self.client()
        client.name = body['name']
        client.description = body['description']
        client.parent_id = parent_id
        client.save_db()
        return client

    # CLIENT BY ID
    def get_by_id(self, client_id: int, parent_id: int) -> dict:
        client = self.client.query.filter_by(id=client_id, parent_id=parent_id).first()
        return client

    # GET ALL
    def get_all(self, page: int, per_page: int, parent_id: int) -> dict:
        clients = self.client.query.filter_by(parent_id=parent_id).paginate(page=page, per_page=per_page)
        return self.get_page_items(clients)

    # GET BY NAME
    def get_by_name(self, name: str, parent_id: int or None) -> Client:
        client = self.client.query.filter_by(name=name, parent_id=parent_id).first()
        return client

    # GET BY NAME EXCLUDE ID
    def get_by_name_exclude_id(self, client_id: int, name: str, parent_id: int) -> Client:
        client = self.client.query.filter(Client.id != client_id, Client.name == name, Client.parent_id == parent_id).first()
        return client

