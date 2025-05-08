from flask import Blueprint, request
from src.services.auth_service import AuthService

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login/student", methods=["POST"])
def login_student():
    return AuthService.login_student(request)


@bp_auth.route("/login/professor", methods=["POST"])
def login_professor():
    return AuthService.login_professor(request)
