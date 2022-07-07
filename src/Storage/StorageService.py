from .IStorageRepo import IStorageRepo
from src.__Parents.Service import Service
from ..Firm.IFirmRepo import IFirmRepo
from ..__Parents.Repository import Repository
from flask import g


class StorageService(Service, Repository):
    def __init__(self, storage_repository: IStorageRepo, firm_repository: IFirmRepo):
        self.storage_repository: IStorageRepo = storage_repository
        self.firm_repository: IFirmRepo = firm_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.storage_repository.get_by_code(body['code']):
            return self.response_conflict('код занят')

        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        self.storage_repository.create(body)
        return self.response_created('склад успешно создан')

    # UPDATE
    def update(self, storage_id: int, body: dict) -> dict:
        storage = self.storage_repository.get_by_id(storage_id)
        if not storage:
            return self.response_not_found('склад не найден')

        if not self.firm_repository.get_by_id(firm_id=body['firm_id'], client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        self.storage_repository.update(storage=storage, body=body)
        return self.response_updated('склад обновлен')

    # DELETE
    def delete(self, storage_id: int) -> dict:
        storage = self.storage_repository.get_by_id(storage_id)
        if not storage:
            return self.response_not_found('склад не найден')

        self.storage_repository.delete(storage)
        return self.response_deleted('склад удален')

    # GET BY ID
    def get_by_id(self, storage_id: int) -> dict:
        storage = self.storage_repository.get_by_id(storage_id)
        if not storage:
            return self.response_not_found('склад не найден')

        return self.response_ok({
            'id': storage.id,
            'title': storage.title,
            'code': storage.code,
            'description': storage.description,
            'storekeeper': storage.storekeeper,
            'address': storage.address,
            'firm': self.get_dict_items(storage.firm)
        })

    # GET ALL
    def get_all(self, page: int, per_page: int, firm_id: int or None, code: str or None) -> dict:
        storages = self.storage_repository.get_all(page=page, per_page=per_page, firm_id=firm_id, code=code)
        return self.response_ok(storages)
