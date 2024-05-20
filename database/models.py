from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Base:
    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()


class UsersModel(db.Model, Base):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    # token = db.Column(db.String(256), unique=True)

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        # self.password = generate_password_hash(password)
        self.password = password

    def __repr__(self) -> str:
        return f'id {self.id} username {self.username} email {self.email} password {self.password}'

    @classmethod
    def find_by_email(cls, email: str) -> 'UsersModel':
        return cls.query.filter_by(email=email).first()


class ListsModel(db.Model, Base):
    __tablename__ = "Lists"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, name: str, description: str, user_id: int) -> None:
        self.name = name
        self.description = description
        self.user_id = user_id

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
