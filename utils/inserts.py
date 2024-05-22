from database.models import TasksModel, ListsModel, UsersModel


class TestData:

    def __init__(self, app):
        self.app = app

    test_user = {
        'username': 'user',
        'email': 'test@gmail.com',
        'password': '123'
    }

    def get_first_id_list(self) -> int:
        with self.app.app_context():
            return ListsModel.query.first().id

    def get_first_id_task(self) -> int:
        with self.app.app_context():
            return TasksModel.query.first().id

    @property
    def tasks_list(self) -> dict[str, str | int]:
        with self.app.app_context():
            tasks_list = {
                'name': 'test list1',
                'description': 'test desc',
                'user_id': UsersModel.query.first().id
            }
            return tasks_list

    tasks = ['cook food', 'to do work', 'call a girl']

    def insert_test_data(self) -> None:
        with self.app.app_context():
            UsersModel(**self.test_user).save()
            ListsModel(**self.tasks_list).save()
            for task in self.tasks:
                TasksModel(task, ListsModel.query.first().id).save()



