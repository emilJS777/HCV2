from abc import ABC, abstractmethod


class IFirmPermissionRepo(ABC):

    @abstractmethod
    def create(self, user, firm_id: int, client_id: int):
        pass

    @abstractmethod
    def get_by_id(self, firm_permission_id: int):
        pass

