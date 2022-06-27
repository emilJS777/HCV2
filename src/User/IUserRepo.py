from abc import ABC, abstractmethod


class IUserRepo(ABC):

    @abstractmethod
    def create(self, body: dict, client_id: int, permissions: list, firm_permissions: list or None = None):
        pass

    @abstractmethod
    def update(self, user_id: int, body: dict, client_id: int, permissions: list, firm_permissions: list or None = None):
        pass

    @abstractmethod
    def delete(self, user_id: int, client_id: int):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int, client_id: int or None):
        pass

    @abstractmethod
    def get_by_name(self, name: str):
        pass

    @abstractmethod
    def get_by_name_exclude_id(self, user_id: int, name: str, client_id: int):
        pass

    @abstractmethod
    def get_all(self, page: int, per_page: int, position_id: int or None, client_id: int):
        pass

    @abstractmethod
    def get_by_ticket(self, ticket: str):
        pass

    @abstractmethod
    def update_auth(self, user_id: int, body: dict) -> dict:
        pass

    @abstractmethod
    def get_by_first_client_id(self, client_id: int):
        pass

    # @abstractmethod
    # def get_permissions_by_user_id(self, user_id: int, permission_ids: list or None = None):
    #     pass

    @abstractmethod
    def get_by_email_address(self, email_address: str):
        pass

    @abstractmethod
    def get_by_email_address_exclude_id(self, user_id: int, email_address: str):
        pass


