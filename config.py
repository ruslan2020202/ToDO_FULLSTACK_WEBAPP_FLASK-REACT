import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{os.environ.get('DATABASE_USER')}:{os.environ.get('DATABASE_PASSWORD')}@db:3306/ToDo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    FLASK_APP = os.environ.get('FLASK_APP')


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL_TEST')


class ProductionConfig(Config):
    DEBUG = False
