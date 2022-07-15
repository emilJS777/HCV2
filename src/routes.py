from .config import api
from ._Admin.AdminController import *
from .User.UserController import UserController
from .Auth.AuthController import AuthController
from .Client.ClientController import ClientController
from .Firm.FirmController import FirmController
from .Sphere.SphereController import SphereController
from .Position.PositionController import PositionController
from .ProductType.ProductTypeController import ProductTypeController
from .Product.ProductController import ProductController
from .Storage.StorageController import StorageController
from .Unit.UnitController import UnitController
from .IncomeType.IncomeTypeController import IncomeTypeController
from .ExpenseType.ExpenseTypeController import ExpenseTypeController
from .Colleague.ColleagueController import ColleagueController
from .Service.ServiceController import ServiceController
from .Resource.ResourceController import ResourceController
from .Employee.EmployeeController import EmployeeController

api.add_resource(AuthController, "/auth")
api.add_resource(UserController, "/user")
api.add_resource(ClientController, "/client")
api.add_resource(FirmController, "/firm")
api.add_resource(SphereController, "/sphere")
api.add_resource(PositionController, "/position")
api.add_resource(ProductTypeController, "/product_type")
api.add_resource(ProductController, "/product")
api.add_resource(StorageController, "/storage")
api.add_resource(UnitController, "/unit")
api.add_resource(IncomeTypeController, "/income_type")
api.add_resource(ExpenseTypeController, "/expense_type")
api.add_resource(ColleagueController, "/colleague")
api.add_resource(ServiceController, "/service")
api.add_resource(ResourceController, "/resource")
api.add_resource(EmployeeController, "/employee")
