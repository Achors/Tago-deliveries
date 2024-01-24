from flask import Flask
from flask_restful import Api
from models import db, User, Profile, Product, Orders, Store
from flask_migrate import Migrate
from routes.User import User, Users
from routes.Authorization import Authorization, Authorizations
from routes.store import Store, Stores
from routes.orders import Order, Orders
from routes.profile import Profile, Profiles
from routes.Product import Product, Products


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)


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




if __name__ == '__main__':
    app.run(debug=True)