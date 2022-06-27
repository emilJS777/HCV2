from .IFirmRepo import IFirmRepo
from src.__Parents.Service import Service
from flask import g
from ..FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from ..__Parents.Repository import Repository


class FirmService(Service, Repository):
    def __init__(self, firm_repository: IFirmRepo, firm_permission_repository: IFirmPermissionRepo):
        self.firm_repository: IFirmRepo = firm_repository
        self.firm_permission_repository: IFirmPermissionRepo = firm_permission_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.firm_repository.get_by_title(title=body['title'], client_id=g.client_id):
            return self.response_conflict('фирма по данной названии уже существует')

        firm = self.firm_repository.create(body=body, client_id=g.client_id)
        self.firm_permission_repository.create(user=g.user, firm_id=firm.id, client_id=g.client_id)
        return self.response_created('фирма успешно создана')

    # UPDATE
    def update(self, body: dict, firm_id: int) -> dict:
        if not self.firm_repository.get_by_id(firm_id=firm_id, client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        if self.firm_repository.get_by_title_exclude_id(firm_id=firm_id, title=body['title'], client_id=g.client_id):
            return self.response_conflict('фирма по данной названии уже существует')

        self.firm_repository.update(firm_id=firm_id, body=body)
        return self.response_updated('фирма успешно обновлена')

    # DELETE
    def delete(self, firm_id: int) -> dict:
        if not self.firm_repository.get_by_id(firm_id=firm_id, client_id=g.client_id):
            return self.response_not_found('фирма не найдена')

        self.firm_repository.delete(firm_id=firm_id)
        return self.response_deleted('фирма удалена')

    # GET BY ID
    def get_by_id(self, firm_id: int) -> dict:
        firm = self.firm_repository.get_by_id(firm_id=firm_id, client_id=g.client_id)
        if not firm:
            return self.response_not_found('фирма не найдена')
        
        firm.sphere = firm.sphere
        return self.response_ok(self.get_dict_items(firm))

    # GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        firms = self.firm_repository.get_all(page=page, per_page=per_page, client_id=g.client_id)
        return self.response_ok(firms)
