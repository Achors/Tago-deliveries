from flask import Blueprint
from config import db
from flask_restful import Api
from User import UserResource, UsersResource
from Authorization import AuthorizationResource, AuthorizationsResource
from store import StoreResource, StoresResource
from orders import OrderResource, OrdersResource
from profile import ProfileResource, ProfilesResource
from Product import ProductResource, ProductsResource

routes = Blueprint('routes', __name__)
api = Api(routes)

api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(UsersResource, '/users')

api.add_resource(AuthorizationResource, '/authorization/<int:authorization_id>')
api.add_resource(AuthorizationsResource, '/authorizations')

api.add_resource(ProfileResource, '/profile/<int:profile_id>')
api.add_resource(ProfilesResource, '/profiles')

api.add_resource(ProductResource, '/product/<int:product_id>')
api.add_resource(ProductsResource, '/products')

api.add_resource(OrderResource, '/order/<int:order_id>')
api.add_resource(OrdersResource, '/orders')  

api.add_resource(StoreResource, '/store/<int:store_id>')
api.add_resource(StoresResource, '/stores')
