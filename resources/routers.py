from flask_restful import Resource
from database.models import TodoList
from flask import jsonify, make_response, request
from schemas.sheme import todo_schema, todos_schema


class TodoTask(Resource):
    def get(self):
        data = TodoList.query.all()
        if not data:
            return make_response(jsonify({'message': 'not found tasks'}), 204)
        else:
            return todos_schema.dump(data), 200

    def post(self):
        try:
            req_data = request.get_json()
            data = TodoList(req_data.get('name'))
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception as e:
            return make_response(jsonify({'error': 'failed'}), 400)


class TodoTasks(Resource):
    def get(self, id):
        data = TodoList.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found task'}), 404)
        else:
            return todo_schema.dump(data), 200

    def patch(self, id):
        data = TodoList.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found task'}), 404)
        else:
            if data.status is not True:
                return make_response(jsonify({'error': 'failed'}), 400)
            else:
                data.status = False
                data.save()
                return make_response(jsonify({'message': 'success'}), 200)

    def delete(self, id):
        data = TodoList.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found task'}), 404)
        else:
            data.delete()
            return make_response(jsonify({'message': 'success'}), 200)
