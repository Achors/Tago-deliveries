from models import db


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'  
    SECRET_KEY = 'your_secret_key'
