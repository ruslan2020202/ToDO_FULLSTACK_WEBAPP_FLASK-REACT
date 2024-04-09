from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from backend.database.models import db
from backend.resources.routers import TodoTask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    Migrate(app, db)
    api.add_resource(TodoTask, '/todo/api/v1', strict_slashes=False)
    return app
