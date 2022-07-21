from .IServiceRepo import IServiceRepo
from .ServiceModel import Service
from src.__Parents.Repository import Repository
from sqlalchemy import or_


class ServiceRepository(Repository, IServiceRepo):
    service: Service = Service

    def create(self, body: dict, client_id: int):
        service = self.service()
        service.code = body['code']
        service.title = body['title']
        service.check = body['check']
        service.wholesale_price = body['wholesale_price']
        service.retail_price = body['retail_price']
        service.unit_id = body['unit_id']
        service.client_id = client_id
        service.save_db()

    def update(self, service: Service, body: dict):
        service.code = body['code']
        service.title = body['title']
        service.check = body['check']
        service.wholesale_price = body['wholesale_price']
        service.retail_price = body['retail_price']
        service.unit_id = body['unit_id']
        service.update_db()

    def delete(self, service: Service):
        service.delete_db()

    def get_by_id(self, service_id: int, client_id: int) -> Service:
        service = self.service.query.filter_by(id=service_id, client_id=client_id).first()
        service.unit = service.unit
        return service

    def get_all(self, page: int, per_page: int, search: str or None, client_id: int) -> list[dict]:
        services = self.service.query.filter_by(client_id=client_id)\
            .filter(or_(self.service.title.like(f"%{search}%"), self.service.code.like(f"%{search}%")) if search else self.service.id.isnot(None))\
            .paginate(page=page, per_page=per_page)

        for service in services.items:
            service.unit = service.unit
        return services

    def get_by_title(self, title: str, client_id: int) -> Service:
        service = self.service.query.filter_by(title=title, client_id=client_id).first()
        return service

    def get_by_title_exclude_id(self, service_id: int, title: str, client_id: int) -> Service:
        service = self.service.query.filter(self.service.id != service_id,
                                            self.service.title == title,
                                            self.service.client_id == client_id).first()
        return service

    def get_by_code(self, code: str, client_id: int) -> Service:
        service = self.service.query.filter_by(code=code, client_id=client_id).first()
        return service

    def get_by_code_exclude_id(self, service_id: int, code: str, client_id: int) -> Service:
        service = self.service.query.filter(self.service.id != service_id,
                                            self.service.code == code,
                                            self.service.client_id == client_id).first()
        return service
