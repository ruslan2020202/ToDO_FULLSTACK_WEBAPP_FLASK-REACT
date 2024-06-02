from flask_restful import Resource
from flask import jsonify, make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from database.models import TasksModel, ListsModel, UsersModel
from schemas.sheme import *


class TodoTasks(Resource):
    @jwt_required()
    def post(self):
        """
        Create a new task
        """
        try:
            req_data = request.get_json()
            data = TasksModel(req_data.get('name'), req_data.get('list_id'))
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception:
            return make_response(jsonify({'error': 'failed'}), 400)


class TodoTask(Resource):
    @jwt_required()
    def patch(self, id):
        """
        Changing task status
        """
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

    @jwt_required()
    def delete(self, id):
        """
        Deleting a task
        """
        data = TasksModel.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found task'}), 404)
        else:
            data.delete()
            return make_response(jsonify({'message': 'success'}), 200)


class TodoLists(Resource):

    @jwt_required()
    def get(self):
        """
        get all lists
        """
        try:
            data = ListsModel.query.filter_by(user_id=get_jwt_identity()).all()
            if not data:
                return make_response(jsonify({'error': 'not found lists'}), 404)
            else:
                return TodoListSchema.schema_many(data), 200
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 400)

    @jwt_required()
    def post(self):
        """
        create a new list
        """
        try:
            req_data = request.get_json()
            data = ListsModel(req_data.get('name'), req_data.get('description'), get_jwt_identity())
            data.save()
            return make_response(jsonify({'message': 'success'}), 201)
        except Exception as e:
            return make_response(jsonify({'error': 'failed'}), 400)


class TodoList(Resource):
    @jwt_required()
    def get(self, id):
        """
        get all tasks from the list
        """
        data = TasksModel.query.filter_by(list_id=id).all()
        if not data:
            return make_response(jsonify({'message': 'not found task in list'}), 404)
        else:
            return TodoTaskSchema.schema_many(data)

    @jwt_required()
    def delete(self, id):
        """
        delete a list
        """
        data = ListsModel.query.get(id)
        if not data:
            return make_response(jsonify({'error': 'not found list'}), 404)
        else:
            data.delete()
            return make_response(jsonify({'message': 'success'}), 200)


class UserInfo(Resource):
    @jwt_required()
    def get(self):
        data = UsersModel.query.get(get_jwt_identity())
        return UserSchema.schema_many(data)


