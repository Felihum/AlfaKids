from flask import Flask, request, jsonify
from db import database
from config import app_config, app_active
from flask_migrate import Migrate
from views.student_view import bp_student
from views.accountable_view import bp_accountable
from views.activity_view import bp_activity
from views.subject_view import bp_subject
from views.question_view import bp_question
from views.professor_view import bp_professor
from views.classroom_view import bp_classroom
from views.student_answer_view import bp_answer
from views.email_view import bp_email
from views.auth_view import bp_auth
from views.student_accomplishment_view import bp_accomplishment
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mail import mail

config = app_config.get(app_active)


def create_app():
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config.JWT_ACCESS_TOKEN_EXPIRES

    app.config['MAIL_SERVER'] = config.MAIL_SERVER
    app.config['MAIL_PORT'] = config.MAIL_PORT
    app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL

    app.register_blueprint(bp_student)
    app.register_blueprint(bp_accountable)
    app.register_blueprint(bp_activity)
    app.register_blueprint(bp_subject)
    app.register_blueprint(bp_question)
    app.register_blueprint(bp_professor)
    app.register_blueprint(bp_classroom)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_accomplishment)
    app.register_blueprint(bp_answer)
    app.register_blueprint(bp_email)

    database.init_app(app)
    mail.init_app(app)

    migrate = Migrate()

    migrate.init_app(app, database)

    jwt = JWTManager(app)

    CORS(app)

    with app.app_context():
        from models.student.student import Student
        from models.subject.subject import Subject
        from models.activity.activity import Activity
        from models.question.question import Question
        from models.question.discursive_question import DiscursiveQuestion
        from models.question.objective_question import ObjectiveQuestion
        from models.professor.professor import Professor
        from models.accountable.accountable import Accountable
        from models.activity_distribution.activity_distribution import ActivityDistribution
        from models.class_allocation.class_allocation import ClassAllocation
        from models.student_accomplishment.student_accomplishment import StudentAccomplishment
        from models.student_answer.student_answer import StudentAnswer

    return app
