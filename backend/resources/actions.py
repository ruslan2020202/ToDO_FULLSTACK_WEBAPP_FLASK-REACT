from backend.resources.routers import *
from flask_restful import Api


def register_actions(app):
    api = Api(app)
    api.add_resource(TodoTask, "/todo/api/v1/tasks", strict_slashes=False)
    api.add_resource(TodoTasks, "/todo/api/v1/tasks/<id>", strict_slashes=False)

