import os
from dotenv import load_dotenv
from flask import Flask
from src.config import app_config, app_active
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

def create_app(test_config=None):
    load_dotenv()

    config = app_config.get(app_active)

    app = Flask(__name__, template_folder='templates')

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.secret_key = config.SECRET
        app.config.from_object(config)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from src.views.student_view import bp_student
    from src.views.accountable_view import bp_accountable
    from src.views.activity_view import bp_activity
    from src.views.subject_view import bp_subject
    from src.views.question_view import bp_question
    from src.views.professor_view import bp_professor
    from src.views.classroom_view import bp_classroom
    from src.views.student_answer_view import bp_answer
    from src.views.auth_view import bp_auth
    from src.views.email_view import bp_email
    from src.views.student_accomplishment_view import bp_accomplishment

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

    from src.db import database

    database.init_app(app)

    migrate = Migrate()

    migrate.init_app(app, database)

    jwt = JWTManager(app)

    CORS(app)

    with app.app_context():
        pass

    return app