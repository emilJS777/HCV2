from src.__Parents.Service import Service
from .ISphereRepo import ISphereRepo


class SphereService(Service):
    def __init__(self, sphere_repository: ISphereRepo):
        self.sphere_repository = sphere_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.sphere_repository.get_by_name(name=body['name']):
            return self.response_conflict('сфера уже существует')

        self.sphere_repository.create(body=body)
        return self.response_created('сфера успешно создана')

    # UPDATE
    def update(self, body: dict, sphere_id: int) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id)
        if not sphere:
            return self.response_not_found('сфера не найдена')

        self.sphere_repository.update(sphere=sphere, body=body)
        return self.response_updated('сфера успешно обновлена')

    # DELETE
    def delete(self, sphere_id: int) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id)
        if not sphere:
            return self.response_not_found('сфера не найдена')

        self.sphere_repository.delete(sphere=sphere)
        return self.response_deleted('сфера успешно удалена')

    # GET BY ID
    def get_by_id(self, sphere_id: int) -> dict:
        sphere = self.sphere_repository.get_by_id(sphere_id)
        if not sphere:
            return self.response_not_found('сфера не найдена')

        return self.response_ok({'id': sphere.id, 'name': sphere.name, 'description': sphere.description})

    # GET ALL
    def get_all(self) -> dict:
        spheres = self.sphere_repository.get_all()
        return self.response_ok(spheres)
