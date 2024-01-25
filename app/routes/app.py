from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db
from .route import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


CORS(app)


app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
