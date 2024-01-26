from models import db
import jwt
import datetime


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  
    SECRET_KEY = 'cK9A8a5-HXa--zk8qNLYi1KbDeezzLPYRf-b4sZh6yE'


    def generate_token(app, username):
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        token = jwt.encode({'username': username, 'exp': expiration_date}, app.config['SECRET_KEY'], algorithm='HS256')
        return token
