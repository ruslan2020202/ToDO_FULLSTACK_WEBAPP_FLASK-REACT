from flask_restful import Api

from resources.routers import *
from .auth import *


def register_actions(app):
    api = Api(app)
    api.add_resource(TodoTasks, "/api/v1/task", strict_slashes=False) # post
    api.add_resource(TodoTask, "/api/v1/task/<id>", strict_slashes=False) # path, delete
    api.add_resource(TodoLists, "/api/v1/lists", strict_slashes=False) # get post
    api.add_resource(TodoList, "/api/v1/list/<id>", strict_slashes=False) # get delete
    api.add_resource(SignUp, "/api/v1/auth/signup", strict_slashes=False)
    api.add_resource(AuthLogin, "/api/v1/auth/login", strict_slashes=False)
