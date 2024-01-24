from flask import Blueprint
from flask_restful import Api
from app.models import db, User, Profile, Product, Orders, Store
from app.routes.User import User, Users
from app.routes.Authorization import Authorization, Authorizations
from app.routes.store import Store, Stores
from app.routes.orders import Order, Orders
from app.routes.profile import Profile, Profiles
from app.routes.Product import Product, Products

routes = Blueprint('routes', __name__)
api = Api(routes)

api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Users, '/users')

api.add_resource(Authorization, '/authorization/<int:authorization_id>')
api.add_resource(Authorizations, '/authorizations')

api.add_resource(Profile, '/profile/<int:profile_id>')
api.add_resource(Profiles, '/profiles')

api.add_resource(Product, '/product/<int:product_id>')
api.add_resource(Products, '/products')

api.add_resource(Order, '/order/<int:order_id>')
api.add_resource(Orders, '/orders')  

api.add_resource(Store, '/store/<int:store_id>')
api.add_resource(Stores, '/stores')
