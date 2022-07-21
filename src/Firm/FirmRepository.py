from src.Firm.IFirmRepo import IFirmRepo
from src.__Parents.Repository import Repository
from .FirmModel import Firm
from flask import g
from sqlalchemy import or_



class FirmRepository(Repository, IFirmRepo):
    firm: Firm = Firm

    def create(self, body: dict, client_id: int) -> Firm:
        firm = self.firm()
        firm.title = body['title']
        firm.email_address = body['email_address']
        firm.activity_address = body['activity_address']
        firm.legal_address = body['legal_address']
        firm.phone_number = body['phone_number']

        firm.hvhh = body['hvhh']
        firm.tax_area_code = body['tax_area_code']
        firm.chapter_registration_number = body['chapter_registration_number']
        firm.insurer_account_number = body['insurer_account_number']

        firm.sphere_id = body['sphere_id']

        firm.client_id = client_id
        firm.save_db()
        return firm

    def update(self, firm_id: int, body: dict) -> firm:
        firm = self.firm.query.filter_by(id=firm_id).first()
        firm.title = body['title']
        firm.email_address = body['email_address']
        firm.activity_address = body['activity_address']
        firm.legal_address = body['legal_address']
        firm.phone_number = body['phone_number']

        firm.hvhh = body['hvhh']
        firm.tax_area_code = body['tax_area_code']
        firm.chapter_registration_number = body['chapter_registration_number']
        firm.insurer_account_number = body['insurer_account_number']

        firm.sphere_id = body['sphere_id']
        firm.update_db()
        return firm

    def delete(self, firm_id: int) -> Firm:
        firm = self.firm.query.filter(Firm.id == firm_id).first()
        firm.delete_db()
        return firm

    def get_by_id(self, firm_id: int, client_id: int) -> Firm:
        firm = self.firm.query.filter(Firm.id.in_(permission.firm_id for permission in g.user.firm_permissions))\
            .filter_by(id=firm_id, client_id=client_id).first()
        return firm

    def get_all(self, page: int, per_page: int, search: str or None, sphere_id: int or None, client_id: int) -> dict:
        firms = self.firm.query.filter_by(client_id=client_id)\
            .filter(self.firm.id.in_(g.allowed_firm_ids))\
            .filter(self.firm.sphere_id == sphere_id if sphere_id else self.firm.sphere_id.isnot(None))\
            .filter(or_(self.firm.title.like(f"%{search}%"), self.firm.email_address.like(f"%{search}%")) if search else self.firm.id.isnot(None))\
            .paginate(page=page, per_page=per_page)

        for firm in firms.items:
            firm.sphere = firm.sphere
        return self.get_page_items(firms)

    def get_by_title(self, title: str, client_id: int) -> Firm:
        firm = self.firm.query.filter_by(title=title, client_id=client_id).first()
        return firm

    def get_by_title_exclude_id(self, firm_id: int, title: str, client_id: int) -> Firm:
        firm = self.firm.query.filter(
            Firm.title == title,
            Firm.client_id == client_id,
            Firm.id != firm_id).first()
        return firm

