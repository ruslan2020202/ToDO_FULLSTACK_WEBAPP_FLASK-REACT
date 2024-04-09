from flask_restful import Resource
from backend.database.models import TodoList
from flask import jsonify


class TodoTask(Resource):
    def get(self):
        data = TodoList.query.all()
        print(data)
        json_data = list(map(lambda x: x.to_json_data(), data))
        print(json_data)
        return json_data, 200

    def post(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
