from flask_restful import Resource
from database.models import UsersModel
from flask import jsonify, make_response, request
from schemas.sheme import *
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class SignUp(Resource):
    def post(self):
        try:
            username = request.json.get('username')
            email = request.json.get('email')
            password = request.json.get('password')
            user = UsersModel.find_by_email(email)
            if not user:
                UsersModel(username, email, password).save()
                return make_response(jsonify({'message': 'success'}), 201)
            else:
                return make_response(jsonify({'message': 'user already exists'}), 409)
        except Exception as e:
            make_response(jsonify({'message': str(e)}))


class AuthLogin(Resource):
    def post(self):
        try:
            email = request.json.get('email')
            password = request.json.get('password')
            user = UsersModel.find_by_email(email)
            # if not user or check_password_hash(user.password, password):
            if not user or user.password != password:
                return make_response(jsonify({'message': 'not correct data'}), 401)
            else:
                token = create_access_token(identity=user.id)
                return make_response(jsonify({'message': 'success', 'user': token}), 200)
        except Exception as e:
            return make_response(jsonify({'message': str(e)}))


class AuthLogout(Resource):
    @jwt_required()
    def post(self):
        pass
