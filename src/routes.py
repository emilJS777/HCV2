from .config import api
from .User.UserController import UserController
from .Auth.AuthController import AuthController
from .Client.ClientController import ClientController
from .Firm.FirmController import FirmController
from .Sphere.SphereController import SphereController
from .Position.PositionController import PositionController

api.add_resource(AuthController, "/auth")
api.add_resource(UserController, "/user")
api.add_resource(ClientController, "/client")
api.add_resource(FirmController, "/firm")
api.add_resource(SphereController, "/sphere")
api.add_resource(PositionController, "/position")
