from backend.database.models import db, TodoList
from backend.wsgi import app

test_data = ['come home', 'cook food', 'to do work']

with app.app_context():
    for i in test_data:
        db.session.add(TodoList(i))
    db.session.commit()
