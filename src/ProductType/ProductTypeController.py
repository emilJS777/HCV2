from .ProductTypeRepository import ProductTypeRepository
from .ProductTypeService import ProductTypeService
from src.__Parents.Controller import Controller
from .ProductTypeValidator import product_type_schema
from flask_expects_json import expects_json
from src.Auth.AuthMiddleware import AuthMiddleware
from src.Permission.PermissionMiddleware import PermissionMiddleware


class ProductTypeController(Controller):
    product_type_service = ProductTypeService(product_type_repository=ProductTypeRepository())

    # POST
    @expects_json(product_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('product_type_edit')
    def post(self) -> dict:
        res: dict = self.product_type_service.create(body=self.request.get_json())
        return res

    # PUT
    @expects_json(product_type_schema)
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('product_type_edit')
    def put(self) -> dict:
        res: dict = self.product_type_service.update(product_type_id=self.id,
                                                     body=self.request.get_json())
        return res

    # DELETE
    @AuthMiddleware.check_authorize
    @PermissionMiddleware.check_permission('product_type_edit')
    def delete(self) -> dict:
        res: dict = self.product_type_service.delete(product_type_id=self.id)
        return res

    # GET
    @AuthMiddleware.check_authorize
    def get(self) -> dict:
        if self.id:
            res: dict = self.product_type_service.get_by_id(self.id)
        else:
            res: dict = self.product_type_service.get_all()
        return res
