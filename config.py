import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST_TEST')}:3306/{os.environ.get('DATABASE_NAME_TEST')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    FLASK_APP = os.environ.get('FLASK_APP')


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{os.environ.get('DATABASE_PASSWORD')}@{os.environ.get('DATABASE_HOST')}:3306/{os.environ.get('DATABASE_NAME')}"

