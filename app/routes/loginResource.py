from flask_restful import Resource, Api, reqparse
from flask import Flask, jsonify, request
from .config import generate_token
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cK9A8a5-HXa--zk8qNLYi1KbDeezzLPYRf-b4sZh6yE'
api = Api(app)

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')


        if username == 'example' and password == 'password':
            token = generate_token(username)
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401

class ProtectedResource(Resource):
    def get(self):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            payload = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms=['HS256'])
            return jsonify({'message': f'Welcome, {payload["username"]}!'})
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

api.add_resource(LoginResource, '/login')
api.add_resource(ProtectedResource, '/protected')



if __name__ == '__main__':
    app.run(debug=True)