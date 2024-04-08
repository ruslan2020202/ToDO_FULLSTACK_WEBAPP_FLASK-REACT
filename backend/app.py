from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from backend.database.db import db
from backend.resources.routers import Todo
from backend.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)
    CORS(app)
    import backend.database.models
    db.init_app(app)
    with app.app_context():
        db.create_all()
    Migrate(app, db)
    api.add_resource(Todo, '/todo/api/v1', strict_slashes=False)
    return app
