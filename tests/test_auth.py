from .test_base import *


def test_signup(client):
    data = {
        'username': faker.first_name(),
        'email': faker.email(),
        'password': faker.password()
    }
    res = client.post('api/v1/auth/signup', json=data)
    assert res.status_code == 201


def test_login(client):
    res = client.post('api/v1/auth/login', json=TestData.test_user)
    assert res.status_code == 200
