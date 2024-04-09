from backend.resources.routers import TodoTask
from flask_restful import Api


def register_actions(app):
    api = Api(app)
    api.add_resource(TodoTask, '/todo/api/v1/tasks', strict_slashes=False)
