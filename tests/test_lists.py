from .test_base import *


def test_all_lists(client, auth):
    response = client.get('/api/v1/lists', headers={'Authorization': f'Bearer {auth}'})
    assert response.status_code == 200


def test_new_list(client, auth, app):
    new_list = {
        'name': 'task list',
        'description': 'new tasks list new',
        'user_id': TestData(app).tasks_list.get('user_id')
    }
    response = client.post('/api/v1/lists', headers={'Authorization': f'Bearer {auth}'}, json=new_list)
    assert response.status_code == 201


def test_all_tasks(client, auth, app):
    id = TestData(app).get_first_id_list()
    response = client.get(f'/api/v1/list/{id}', headers={'Authorization': f'Bearer {auth}'})
    assert response.status_code == 200


def test_delete_list(client, auth, app):
    id = TestData(app).get_first_id_list()
    response = client.delete(f'/api/v1/list/{id}', headers={'Authorization': f'Bearer {auth}'})
    assert response.status_code == 200
