from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import database
from config import app_config, app_active
from flask_migrate import Migrate
from views.student_view import bp_student

config = app_config.get(app_active)

def create_app():
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    app.register_blueprint(bp_student)

    database.init_app(app)

    migrate = Migrate()

    migrate.init_app(app, database)

    with app.app_context():
        from models.student.student import Student
        from models.subject.subject import Subject
        from models.activity.activity_objective import ActivityObjective
        from models.activity.activity_discursive import ActivityDiscursive
        from models.accountable.accountable import Accountable
        #database.create_all()

    return app
