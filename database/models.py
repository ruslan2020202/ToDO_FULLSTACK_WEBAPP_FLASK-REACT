from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Base:
    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


class ListsModel(db.Model, Base):
    __tablename__ = "Lists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def __repr__(self) -> str:
        return f'id: {self.id}, name: {self.name}, description: {self.description}'


class TasksModel(db.Model, Base):
    __tablename__ = 'Tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    time = db.Column(db.String(25), nullable=False, default=datetime.now().strftime("%I:%M %p"))
    list_id = db.Column(db.Integer, db.ForeignKey('Lists.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, name: str, list_id: int) -> None:
        self.name = name
        self.list_id = list_id

    def __repr__(self) -> str:
        return f'id: {self.id}, name: {self.name}, status: {self.status}, time: {self.time}, list_id: {self.list_id}'
