from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import database
from config import app_config, app_active
from flask_migrate import Migrate

config = app_config.get(app_active)

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    database.init_app(app)

    migrate = Migrate()

    migrate.init_app(app, database)

    with app.app_context():
        from models.client.student import Student
        from models.client.professor import Professor
        from models.subject.subject import Subject
        from models.classroom.classroom import Classroom
        from models.activity.activity_objective import ActivityObjective
        from models.activity.activity_discursive import ActivityDiscursive
        from models.accountable.accountable import Accountable

    return app
