from app import app, db
from flask import jsonify, request
from app.models import User, Profile, Product, Orders, Store


@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [{'username': user.username, 'email': user.email} for user in users]})
