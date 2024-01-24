from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ..config import Config
from flask import Blueprint



from .routes import routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes)
    app.config.from_object(Config)
    db = SQLAlchemy(app)

    return app
