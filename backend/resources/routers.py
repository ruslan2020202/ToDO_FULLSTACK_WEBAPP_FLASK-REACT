from flask_restful import Resource
from backend.database.models import TodoList
from flask import jsonify, make_response, request


class TodoTask(Resource):
    def get(self):
        data = TodoList.query.all()
        print(data)
        if not data:
            return make_response(jsonify({'error': 'not found tasks'}), 404)
        else:
            data = list(map(lambda x: x.to_json_data(), data))
            return data, 200

    def post(self):
        try:
            req_data = request.get_json()
            data = TodoList(req_data.get('name'))
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception as e:
            return make_response(jsonify({'error': f'failed'}), 400)


class TodoTasks(Resource):
    def get(self, id):
        data = TodoList.query.get_or_404(id)
        return data.to_json_data()

    def patch(self, id):
        pass

    def delete(self, id):
        pass
