from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity

bp_auth = Blueprint("auth", __name__, url_prefix="/auth")


@bp_auth.route("/login/student", methods=["POST"])
def login_student():
    return AuthService.login_student(request)


@bp_auth.route("/login/professor", methods=["POST"])
def login_professor():
    return AuthService.login_professor(request)
