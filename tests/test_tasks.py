from .test_base import *


def test_new_task(client, auth, app):
    new_task = {
        'name': f'new_task by {faker.first_name()}',
        'list_id': TestData(app).get_first_id_list()
    }
    response = client.post('/api/v1/task', headers={'Authorization': f'Bearer {auth}'}, json=new_task)

    assert response.status_code == 201


def test_change_task(client, auth, app):
    id = TestData(app).get_first_id_task()
    response = client.patch(f'/api/v1/task/{id}', headers={'Authorization': f'Bearer {auth}'})
    assert response.status_code == 200


def test_delete_task(client, auth, app):
    id = TestData(app).get_first_id_task()
    response = client.delete(f'/api/v1/task/{id}', headers={'Authorization': f'Bearer {auth}'})
    assert response.status_code == 200
