from .IClientRepo import IClientRepo
from ..__Parents.Service import Service
from flask import g


class ClientService(Service):
    def __init__(self, client_repository: IClientRepo):
        self._client_repository: IClientRepo = client_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self._client_repository.get_by_name(body['name'], parent_id=g.client_id):
            return self.response_conflict('клиент с таким именем существует')

        self._client_repository.create(body, parent_id=g.client_id)
        return self.response_created('клиент создан')

    # UPDATE
    def update(self, client_id: int, body: dict) -> dict:
        client = self._client_repository.get_by_id(client_id, parent_id=g.client_id)
        if not client:
            return self.response_not_found('клиент не найден')

        if self._client_repository.get_by_name_exclude_id(client_id=client_id, name=body['name'], parent_id=g.client_id):
            return self.response_updated('клиент с таким именем существует')

        client.name = body['name']
        client.description = body['description']
        client.update_db()

        return self.response_updated('клиент обновлен')

    # DELETE
    def delete(self, client_id: int) -> dict:
        client = self._client_repository.get_by_id(client_id, parent_id=g.client_id)
        if not client:
            return self.response_not_found('клиент не найден')

        client.delete_db()
        return self.response_deleted('клиент удален')

    # GET BY ID
    def get_by_id(self, client_id: int) -> dict:
        client = self._client_repository.get_by_id(client_id, parent_id=g.client_id)
        if not client:
            return self.response_not_found('клиент не найден')

        return self.response_ok({'id': client.id, 'name': client.name, 'description': client.description})

    # GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        clients = self._client_repository.get_all(
            page=page,
            per_page=per_page,
            parent_id=g.client_id)

        return self.response_ok(clients)
