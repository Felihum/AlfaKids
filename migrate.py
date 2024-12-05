from flask_migrate import Migrate
from app import create_app
from db import database
from flask import Flask
from config import app_config, app_active

config = app_config.get(app_active)

app = Flask(__name__)

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
    from models.activity.activity_objective import Objective
    from models.activity.activity_discursive import Discursive
    from models.accountable.accountable import Accountable

if __name__ == "__main__":
    app.run()
