import pytest
import config as config
from api import create_app
from database.models import *
from tests.inserts import insert_test_data


def find_id(app):
    with app.app_context():
        id_task = TasksModel.query.first().id
        return id_task


@pytest.fixture
def app():
    app = create_app(config.TestingConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        insert_test_data(app)
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client


def test_get_tasks(client):
    response = client.get('/todo/api/v1/tasks')
    assert response.status_code == 200


def test_get_task_by_id(client, app):
    res = client.get(f'/todo/api/v1/tasks/{find_id(app)}')
    assert res.status_code == 200


def test_add_task(client):
    data = {'name': 'Test task'}
    res = client.post('/todo/api/v1/tasks', json=data)
    assert res.status_code == 201


def test_update_task(client, app):
    res = client.patch(f'/todo/api/v1/tasks/{find_id(app)}')
    assert res.status_code == 200


def test_delete_task(client, app):
    res = client.delete(f'/todo/api/v1/tasks/{find_id(app)}')
    assert res.status_code == 200
