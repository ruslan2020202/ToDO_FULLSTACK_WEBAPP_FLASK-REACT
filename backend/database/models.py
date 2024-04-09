from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TodoList(db.Model):
    __tablename__ = 'todoList'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Id: {self.id}, Name: {self.name}, Status: {self.status}'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def to_json_data(self):
        return {
            "id": self.id,
            'name': self.name,
            'status': self.status
        }
