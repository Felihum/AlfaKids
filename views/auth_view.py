from flask import Blueprint, request
from services.auth_service import AuthService
from services.email_service import EmailService

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")

email_service = EmailService()

@bp_auth.route("/login/student", methods=["POST"])
def login_student():
    return AuthService.login_student(request)

@bp_auth.route("/login/professor", methods=["POST"])
def login_professor():
    return AuthService.login_professor(request)

@bp_auth.route('/request_reset', methods=['POST'])
def request_reset():
    return email_service.request_reset(request)

@bp_auth.route('/reset', methods=['POST'])
def reset_password():
    return email_service.reset_password(request)

