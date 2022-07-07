from .IResourceRepo import IResourceRepo
from ..__Parents.Repository import Repository
from .ResourceModel import Resource
from flask import g


class ResourceRepository(Repository, IResourceRepo):
    resource: Resource = Resource

    def create(self, body: dict):
        resource = self.resource()
        resource.title = body['title']
        resource.input_date = body['input_date']
        resource.operation_date = body['operation_date']
        resource.hm_type = body['hm_type']
        resource.hm_group = body['hm_group']
        resource.employee_bank_account = body['employee_bank_account']
        resource.location = body['location']
        resource.firm_id = body['firm_id']

        resource.client_id = g.client_id
        resource.save_db()

    def update(self, resource: Resource, body: dict):
        resource.title = body['title']
        resource.input_date = body['input_date']
        resource.operation_date = body['operation_date']
        resource.hm_type = body['hm_type']
        resource.hm_group = body['hm_group']
        resource.employee_bank_account = body['employee_bank_account']
        resource.location = body['location']
        resource.firm_id = body['firm_id']

        resource.client_id = g.client_id
        resource.update_db()

    def delete(self, resource: Resource):
        resource.delete_db()

    def get_by_id(self, resource_id: int) -> Resource:
        resource = self.resource.query.filter(Resource.firm_id.in_(g.allowed_firm_ids),
                                              Resource.id == resource_id,
                                              Resource.client_id == g.client_id).first()
        return resource

    def get_all(self, page: int, per_page: int, firm_id: int or None) -> list[dict]:
        resources = self.resource.query.filter(
            Resource.firm_id.in_(g.allowed_firm_ids),
            Resource.firm_id == firm_id if firm_id else Resource.firm_id.isnot(None),
            Resource.client_id == g.client_id
        ).paginate(page=page, per_page=per_page)
        return self.get_page_items(resources)
    
