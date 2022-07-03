from src.__Parents.Repository import Repository
from src.__Parents.Service import Service
from .IColleagueRepo import IColleagueRepo
from flask import g


class ColleagueService(Service, Repository):

    def __init__(self, colleague_repository: IColleagueRepo):
        self.colleague_repository: IColleagueRepo = colleague_repository

    # CREATE
    def create(self, body: dict) -> dict:
        if self.colleague_repository.get_by_title(title=body['title'], client_id=g.user.client_id):
            return self.response_conflict('название занято')

        self.colleague_repository.create(body, g.user.client_id)
        return self.response_created('коллега создано')

    # UPDATE
    def update(self, colleague_id: int, body: dict) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        self.colleague_repository.update(colleague=colleague, body=body)
        return self.response_updated('коллега обновлено')

    # DELETE
    def delete(self, colleague_id: int) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        self.colleague_repository.delete(colleague)
        return self.response_deleted('коллега удалено')

    # GET BY ID
    def get_by_id(self, colleague_id: int) -> dict:
        colleague = self.colleague_repository.get_by_id(colleague_id, g.user.client_id)

        if not colleague:
            return self.response_not_found('коллега не найдено')

        return self.response_ok(self.get_dict_items(colleague))

    # GET ALL
    def get_all(self, page: int, per_page: int) -> dict:
        colleagues = self.colleague_repository.get_all(
            page=page,
            per_page=per_page,
            client_id=g.user.client_id)

        return self.response_ok(colleagues)
    