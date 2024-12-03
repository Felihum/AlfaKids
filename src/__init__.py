from flask import Flask
from db import db
from dynaconf import FlaskDynaconf


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_mapping(
    #    SECRET_KEY='dev',
    #    SQLALQUEMY_DATABASE_URI="postgresql://postgres:password@localhost:5432/apiPythonDb",
    #    SQLALCHEMY_TRACK_MODIFICATIONS=False
    #)

    FlaskDynaconf(app, settings_files=['settings.toml'])

    if test_config is not None:
        app.config.from_mapping(test_config)

    db.init_app(app)

    return app
