from flask_restful import Resource
from database.models import TasksModel, ListsModel
from flask import jsonify, make_response, request
from schemas.sheme import *


class TodoTasks(Resource):

    def post(self):
        try:
            req_data = request.get_json()
            data = TasksModel(req_data.get('name'), req_data.get('list_id'))
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception:
            return make_response(jsonify({'error': 'failed'}), 400)


class TodoTask(Resource):

    def patch(self, id):
        data = TasksModel.query.get(id)
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
        data = TasksModel.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found task'}), 404)
        else:
            data.delete()
            return make_response(jsonify({'message': 'success'}), 200)


class TodoLists(Resource):

    def get(self):
        data = ListsModel.query.all()
        if not data:
            return make_response(jsonify({'error': 'not found lists'}), 404)
        else:
            return TodoListSchema.schema_many(data), 200

    def post(self):
        try:
            req_data = request.get_json()
            data = ListsModel(req_data.get('name'), req_data.get('description'))
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception as e:
            return make_response(jsonify({'error': 'failed'}), 400)


class TodoList(Resource):
    def get(self, id):
        data = TasksModel.query.filter_by(list_id=id).all()
        if not data:
            return make_response(jsonify({'message': 'not found task in list'}), 404)
        else:
            return TodoTaskSchema.schema_many(data)

    def delete(self, id):
        data = ListsModel.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found list'}), 404)
        else:
            data.delete()
            return make_response(jsonify({'message': 'success'}), 200)
