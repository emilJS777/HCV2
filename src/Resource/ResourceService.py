from .IResourceRepo import IResourceRepo
from ..__Parents.Repository import Repository
from ..__Parents.Service import Service


class ResourceService(Service, Repository):

    def __init__(self, resource_repository: IResourceRepo):
        self.resource_repository: IResourceRepo = resource_repository

    # CREATE
    def create(self, body: dict) -> dict:
        self.resource_repository.create(body=body)
        return self.response_created('ресурс создан успешно')

    # UPDATE
    def update(self, resource_id: int, body: dict) -> dict:
        resource = self.resource_repository.get_by_id(resource_id)
        if not resource:
            return self.response_not_found('ресурс не найден')

        self.resource_repository.update(resource=resource, body=body)
        return self.response_updated('ресурс обновлен')

    # DELETE
    def delete(self, resource_id: int) -> dict:
        resource = self.resource_repository.get_by_id(resource_id)
        if not resource:
            return self.response_not_found('ресурс не найден')

        self.resource_repository.delete(resource)
        return self.response_deleted('ресурс удален')

    # GET BY ID
    def get_by_id(self, resource_id: int) -> dict:
        resource = self.resource_repository.get_by_id(resource_id)
        if not resource:
            return self.response_not_found('ресурс не найден')

        return self.response_ok(self.get_dict_items(resource))

    # GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        resources = self.resource_repository.get_all(page=page, per_page=per_page)
        return self.response_ok(resources)
    
