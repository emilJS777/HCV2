from abc import ABC, abstractmethod


class IPermissionRepo(ABC):

    @abstractmethod
    def create(self, name: str, title: str, firm_id: int or None):
        pass

    @abstractmethod
    def get_by_id(self, permission_id: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def delete_user_permissions_by_user_id(self, user_id: int):
        pass






