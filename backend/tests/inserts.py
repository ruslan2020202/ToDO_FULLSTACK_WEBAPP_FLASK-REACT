from backend.database.models import db, TodoList
from backend.wsgi import app


def insert_test_data():
    test_data = ['come home', 'cook food', 'to do work']

    with app.app_context():
        try:
            for i in test_data:
                db.session.add(TodoList(i))
            db.session.commit()
            print('Successfully inserted test data')
        except Exception as e:
            print(e)


