from src.__Parents.Controller import Controller
from .ColleagueService import ColleagueService
from .ColleagueRepository import ColleagueRepository
from flask_expects_json import expects_json
from .ColleagueValidator import colleague_schema
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class ColleagueController(Controller):
    colleague_service: ColleagueService = ColleagueService(ColleagueRepository())

    # POST
    @expects_json(colleague_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('colleague_edit')
    def post(self) -> dict:
        res: dict = self.colleague_service.create(self.request.get_json())
        return res

    # PUT
    @expects_json(colleague_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('colleague_edit')
    def put(self) -> dict:
        res: dict = self.colleague_service.update(colleague_id=self.id, body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('colleague_edit')
    def delete(self) -> dict:
        res: dict = self.colleague_service.delete(self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('colleague_get')
    def get(self) -> dict:
        if self.id:
            res: dict = self.colleague_service.get_by_id(self.id)
        else:
            res: dict = self.colleague_service.get_all(page=self.page, per_page=self.per_page, search=self.arguments.get('search'))
        return res
