from src.Sphere.ISphereRepo import ISphereRepo
from src.__Parents.Repository import Repository
from .SphereModel import Sphere


class SphereRepository(Repository, ISphereRepo):
    sphere: Sphere = Sphere

    def create(self, body: dict) -> dict:
        sphere = self.sphere()
        sphere.name = body['name']
        sphere.description = body['description']
        sphere.save_db()
        return sphere

    def update(self, sphere: Sphere, body: dict):
        sphere.name = body['name']
        sphere.description = body['description']
        sphere.update_db()

    def delete(self, sphere: Sphere):
        sphere.delete_db()

    def get_by_id(self, sphere_id: int) -> dict:
        sphere = self.sphere.query.filter_by(id=sphere_id).first()
        return sphere

    def get_all(self):
        spheres = self.sphere.query.all()
        return self.get_array_items(spheres)

    def get_by_name(self, name: str) -> Sphere:
        sphere = self.sphere.query.filter_by(name=name).first()
        return sphere

    def get_by_name_exclude_id(self, sphere_id: int, name: str) -> Sphere:
        sphere = self.sphere.query.filter(Sphere.name == name, Sphere.id != sphere_id).first()
        return sphere
