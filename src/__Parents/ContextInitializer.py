from src import logger
from src.Permission.IPermissionRepo import IPermissionRepo
from src.User.UserRepository import UserRepository
from src.User.IUserRepo import IUserRepo
from src.Permission.PermissionRepository import PermissionRepository
from src.Client.ClientRepository import ClientRepository
from src.Client.IClientRepo import IClientRepo
from src.__Parents.Service import Service


class ContextInitializer(Service):
    user_repository: IUserRepo = UserRepository()
    client_repository: IClientRepo = ClientRepository()
    permission_repository: IPermissionRepo = PermissionRepository()

    # USER
    permissions: list[dict] = [{'name': 'user_get', 'title': 'получить пользователей'},
                               {'name': 'user_edit', 'title': 'редактировать пользователей'},
                               # CLIENT
                               {'name': 'client_get', 'title': 'получить клиентов'},
                               {'name': 'client_edit', 'title': 'редактировать клиентов'},
                               # FIRM
                               {'name': 'firm_edit', 'title': 'редактировать фирмы'},
                               # SPHERE
                               {'name': 'sphere_edit', 'title': 'редактировать сферу'},
                               # POSITION
                               {'name': 'position_edit', 'title': 'редактировать позицию'},
                               # PRODUCT TYPE
                               {'name': 'product_type_edit', 'title': 'редактировать тип продукта'}]

    user: dict = {'first_name': 'Admin', 'last_name': 'Adminyan', 'email_address': 'e.pargevich@mail.ru', 'position_id': None}
    client: dict = {'name': 'First client', 'description': 'First client'}

    def __init__(self):
        client = self.client_init()
        user = self.user_init(client_id=client.id)

    # CLIENT INITIALIZER
    def client_init(self):
        client = self.client_repository.get_by_name(self.client['name'], parent_id=None)
        if not client:
            client = self.client_repository.create(body=self.client, parent_id=None)
            logger.info(f"клиент успешно создан")
        return client

    # USER INITIALIZER
    def user_init(self, client_id):
        user = self.user_repository.get_by_first_client_id(client_id)
        permissions = self.permissions_init()

        if not user:
            self.user['ticket'] = self.generate_ticket_code()
            user = self.user_repository.create(body=self.user, client_id=client_id, permissions=permissions)
            logger.info(f"первый пользователь создан, код регистрации {user.ticket}")
        else:
            self.user_repository.update(user_id=user.id, body=self.user, client_id=client_id, permissions=permissions)
        return user

    # PERMISSIONS INITIALIZER
    def permissions_init(self):
        for permission_dict in self.permissions:
            permission = self.permission_repository.get_by_name(permission_dict['name'])
            if not permission:
                permission = self.permission_repository.create(name=permission_dict['name'], title=permission_dict['title'])
                logger.info(f"разрешение по названию {permission.title} успешно создан ")

        permissions = self.permission_repository.get_all()
        return permissions


