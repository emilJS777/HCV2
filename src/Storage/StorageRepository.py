from src.Storage.IStorageRepo import IStorageRepo
from src.Storage.StorageModel import Storage
from src.__Parents.Repository import Repository
from flask import g
from sqlalchemy import or_


class StorageRepository(Repository, IStorageRepo):
    storage: Storage = Storage

    def create(self, body: dict):
        storage: Storage = Storage()
        storage.title = body['title']
        storage.code = body['code']
        storage.description = body['description']
        storage.firm_id = body['firm_id']
        storage.address = body['address']
        storage.storekeeper = body['storekeeper']
        storage.client_id = g.user.client_id
        storage.save_db()

    def update(self, storage: Storage, body: dict):
        storage.title = body['title']
        storage.code = body['code']
        storage.description = body['description']
        storage.firm_id = body['firm_id']
        storage.address = body['address']
        storage.storekeeper = body['storekeeper']
        storage.save_db()

    def delete(self, storage: Storage):
        storage.delete_db()

    def get_by_id(self, storage_id: int) -> Storage:
        storage: Storage = self.storage.query.filter_by(id=storage_id)\
            .filter(Storage.firm_id.in_(g.allowed_firm_ids)).first()
        return storage

    def get_by_code(self, code: str) -> Storage:
        storage: Storage = self.storage.query.filter_by(code=code, client_id=g.user.client_id) \
            .filter(Storage.firm_id.in_(g.allowed_firm_ids)).first()
        return storage

    def get_all(self, page: int, per_page: int, firm_id: int or None, search: str or None):
        storages = self.storage.query.filter(Storage.firm_id.in_(g.allowed_firm_ids),
                                             Storage.firm_id == firm_id if firm_id else Storage.firm_id.isnot(None),
                                             Storage.client_id == g.user.client_id)\
                                     .filter(or_(Storage.title.like(f"%{search}%"), Storage.code.like(f"%{search}%")) if search else Storage.id.isnot(None))\
            .paginate(page=page, per_page=per_page)
        for storage in storages.items:
            storage.firm = storage.firm
        return self.get_page_items(storages)
