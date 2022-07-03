from src.__Parents.Repository import Repository
from .IColleagueRepo import IColleagueRepo
from .ColleagueModel import Colleague


class ColleagueRepository(Repository, IColleagueRepo):
    colleague: Colleague = Colleague

    def create(self, body: dict, client_id: int):
        colleague = self.colleague()
        colleague.title = body['title']
        colleague.code = body['code']
        colleague.activity_address = body['activity_address']
        colleague.phone_number = body['phone_number']
        colleague.hvhh = body['hvhh']
        colleague.legal_address = body['legal_address']

        colleague.client_id = client_id
        colleague.save_db()

    def update(self, colleague: Colleague, body: dict):
        colleague.title = body['title']
        colleague.code = body['code']
        colleague.activity_address = body['activity_address']
        colleague.phone_number = body['phone_number']
        colleague.hvhh = body['hvhh']
        colleague.legal_address = body['legal_address']
        colleague.update_db()

    def delete(self, colleague: Colleague):
        colleague.delete_db()

    def get_by_id(self, colleague_id: int, client_id: int) -> Colleague:
        colleague = self.colleague.query.filter_by(id=colleague_id, client_id=client_id).first()
        return colleague

    def get_by_title(self, title: str, client_id: int) -> Colleague:
        colleague = self.colleague.query.filter_by(title=title, client_id=client_id).first()
        return colleague

    def get_by_title_exclude_id(self, colleague_id: int, title: str, client_id: int) -> Colleague:
        colleague = self.colleague.query.filter(self.colleague.title == title,
                                                self.colleague.client_id == client_id,
                                                self.colleague.id != colleague_id).first()
        return colleague

    def get_all(self, page: int, per_page: int, client_id: int) -> dict:
        colleagues = self.colleague.query.filter_by(client_id=client_id).paginate(page=page, per_page=per_page)
        return self.get_page_items(colleagues)
