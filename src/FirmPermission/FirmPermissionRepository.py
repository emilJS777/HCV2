from src.FirmPermission.IFirmPermissionRepo import IFirmPermissionRepo
from src.__Parents.Repository import Repository
from .FirmPermissionModel import FirmPermission, UserFirmPermission


class FirmPermissionRepository(Repository, IFirmPermissionRepo):
    firm_permission: FirmPermission = FirmPermission
    user_firm_permission: UserFirmPermission = UserFirmPermission

    #                         PRODUCT
    firm_permissions: dict = [{'name': 'product_edit', 'title': 'редактировать продукт'},
                              {'name': 'product_get', 'title': 'получить продукт'},

                              {'name': 'storage_edit', 'title': 'редактировать хранилище'},
                              {'name': 'storage_get', 'title': 'получить хранилище'},

                              {'name': 'employee_edit', 'title': 'редактировать работников'},
                              {'name': 'employee_get', 'title': 'получить работников'}]

    def create(self, user, firm_id: int, client_id: int):
        firm_permission_list: list = []
        for firm_permission in self.firm_permissions:
            firm_permission_model = self.firm_permission()
            firm_permission_model.name = firm_permission['name']
            firm_permission_model.title = firm_permission['title']
            firm_permission_model.client_id = client_id
            firm_permission_model.firm_id = firm_id
            firm_permission_model.users.append(user)
            firm_permission_list.append(firm_permission_model)
        self.firm_permission.save_all_db(firm_permission_list)

    def get_by_id(self, firm_permission_id: int) -> FirmPermission:
        firm_permission = self.firm_permission.query.filter_by(id=firm_permission_id).first()
        return firm_permission

