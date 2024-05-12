from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class TodoList(db.Model):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    time = db.Column(db.String(25), nullable=False, default=datetime.now().strftime("%I:%M %p"))

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'id: {self.id}, name: {self.name}, status: {self.status}, time: {self.time}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
