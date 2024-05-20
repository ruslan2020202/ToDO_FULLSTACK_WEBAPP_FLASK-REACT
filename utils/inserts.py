from database.models import TasksModel, ListsModel, UsersModel

from faker import Faker

faker = Faker()


def insert_test_data(app):
    tasks = ['cook food', 'to do work', 'call a girl']
    test_data = {
        'users': [(faker.name(), faker.email(), faker.password()) for _ in range(3)],
        'task_lists': [(f'list{i}', faker.text(25), i) for i in range(1, 4)],
        'tasks': [(tasks[i], i+1) for i in range(3)]
    }

    with app.app_context():
        for i in test_data.get('users'):
            UsersModel(i[0], i[1], i[2]).save()
        for i in test_data.get('task_lists'):
            ListsModel(i[0], i[1], int(i[2])).save()
        for i in test_data.get('tasks'):
            TasksModel(i[0], int(i[1])).save()






