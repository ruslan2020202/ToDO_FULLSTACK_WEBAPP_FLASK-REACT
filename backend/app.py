from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from backend.database.models import *
from backend.resources.actions import register_actions


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    Migrate(app, db)
    register_actions(app)
    return app

