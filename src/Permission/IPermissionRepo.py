from abc import ABC, abstractmethod


class IPermissionRepo(ABC):

    @abstractmethod
    def create(self, name: str, title: str, firm: bool, firm_id: int or None):
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






