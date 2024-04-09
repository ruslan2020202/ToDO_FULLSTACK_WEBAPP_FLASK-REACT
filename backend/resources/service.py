from backend.database.models import TodoList
from backend.run import app


class ToDoCore():
    pass


with app.app_context():
    data_all = TodoList.query.first()
    print(data_all)
