from flask import Blueprint, request
from services.email_service import EmailService

bp_email = Blueprint("email", __name__, url_prefix="/email")

@bp_email.route("/submit", methods=["POST"])
def submit():
    return EmailService.submit(request)
