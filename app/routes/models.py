from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    profile = db.relationship('Profile', backref='user', lazy=True)
    orders = db.relationship('Orders', backref='user', lazy=True)

class Profile(db.Model, SerializerMixin):
    __tablename__ = "profile"
    
    profile_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


class Product(db.Model, SerializerMixin):
    __tablename__ = "product"

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


class Orders(db.Model, SerializerMixin):
    __tablename__ = "order"

    order_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer(50), nullable=False)
    date = db.Column(db.Varchar(50), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)


class Store(db.Model, SerializerMixin):
    __tablename__ = "store"

    store_id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)



class Authorization(db.Model, SerializerMixin):
    __tablename__="authorization"

    authorization_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    last_login = db.Column(db.DateTime)

    user = db.relationship('User', backref=db.backref('authorizations', lazy=True))


