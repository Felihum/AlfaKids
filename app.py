from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
from config import app_config, app_active

config = app_config.get(app_active)

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALQUEMY_DATABASE_URI'] = config.SQLALQUEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello World!'

    return app
