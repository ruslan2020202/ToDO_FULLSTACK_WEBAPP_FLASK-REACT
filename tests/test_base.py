import pytest
from faker import Faker

import config as config
from api import create_app
from database.models import *
from utils.inserts import TestData

faker = Faker()


@pytest.fixture
def app():
    app = create_app(config.TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        TestData(app).insert_test_data()
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client


@pytest.fixture
def auth(client):
    """
    Get a token for routes tests that require authorization
    """
    test_user_login = {
        'email': TestData.test_user.get('email'),
        'password': TestData.test_user.get('password')
    }
    log = client.post('/api/v1/auth/login', json=test_user_login)
    token = log.get_json()['token']
    return token
