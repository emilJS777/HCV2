from .IServiceRepo import IServiceRepo
from ..Unit.IUnitRepo import IUnitRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service
from flask import g


class ServiceService(Service, Repository):

    def __init__(self, service_repository: IServiceRepo, unit_repository: IUnitRepo):
        self.service_repository: IServiceRepo = service_repository
        self.unit_repository: IUnitRepo = unit_repository

    def create(self, body: dict) -> dict:
        if self.service_repository.get_by_code(code=body['code'], client_id=g.client_id):
            return self.response_conflict('код занят')

        if self.service_repository.get_by_title(title=body['title'], client_id=g.client_id):
            return self.response_conflict('название занято')

        if not self.unit_repository.get_by_id(body['unit_id']):
            return self.response_not_found('единица измерения не найдена')

        self.service_repository.create(
            body=body,
            client_id=g.client_id)

        return self.response_created('услуга создана')

    def update(self, service_id: int, body: dict) -> dict:
        service = self.service_repository.get_by_id(service_id=service_id, client_id=g.client_id)
        if not service:
            return self.response_not_found('услуга не найдена')

        if self.service_repository.get_by_code_exclude_id(service_id=service_id, code=body['code'], client_id=g.client_id):
            return self.response_conflict('код занят')

        if self.service_repository.get_by_title_exclude_id(service_id=service_id, title=body['title'], client_id=g.client_id):
            return self.response_conflict('название занято')

        if not self.unit_repository.get_by_id(body['unit_id']):
            return self.response_not_found('единица измерения не найдена')

        self.service_repository.update(service=service, body=body)
        return self.response_updated('услуга обновлена')

    def delete(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id=service_id, client_id=g.client_id)
        if not service:
            return self.response_not_found('услуга не найдена')

        self.service_repository.delete(service)
        return self.response_deleted('услуга удалена')

    def get_by_id(self, service_id: int) -> dict:
        service = self.service_repository.get_by_id(service_id=service_id, client_id=g.client_id)
        if not service:
            return self.response_not_found('услуга не найдена')

        return self.response_ok(self.get_dict_items(service))

    def get_all(self, page: int, per_page: int, code: int or None) -> dict:
        services = self.service_repository.get_all(
            page=page,
            per_page=per_page,
            code=code,
            client_id=g.client_id)
        return self.response_ok(self.get_page_items(services))
