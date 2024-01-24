from flask_restful import Resource, reqparse
from models import db, User
from schema import UserSchema
from flask import jsonify

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class User(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user_schema.dump(user))

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('city', type=str)
        args = parser.parse_args()


        user.name = args['username'] or user.name
        user.email = args['email'] or user.email

        db.session.commit()
        return jsonify(user_schema.dump(user))

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

class Users(Resource):
    def get(self):
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('city', type=str, required=True)
        args = parser.parse_args()

        new_user = User(
            username=args['username'],
            email=args['email'],
            city=args['city']
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify(user_schema.dump(new_user)), 201