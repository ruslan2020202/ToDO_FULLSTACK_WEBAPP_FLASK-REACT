from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from database.models import *
from resources.actions import register_actions
from static.swagger import *
from flask_marshmallow import Marshmallow
from resources.errors import Errors
from sqlalchemy import create_engine


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    CORS(app)
    Migrate(app, db)
    Marshmallow(app)
    register_actions(app)
    app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)
    Errors.register_errors(app)
    create_engine(app.config['DATABASE_URL'], pool_size=10, max_overflow=20)
    return app
