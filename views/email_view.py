from flask import Blueprint, current_app, request, jsonify
from services.email_service import EmailService

    
bp_email = Blueprint('email', __name__)
email_service = EmailService()

@bp_email.before_app_request

def init_email_service():
    email_service.init_email_service(current_app)
    print('yes')


@bp_email.route('/forgot-password', methods=['POST'])
def forgot_password():
    """Endpoint para solicitar recuperação de senha"""
    return email_service.request_reset(request)

@bp_email.route('/reset-password', methods=['POST'])
def reset_password():
    """Endpoint para redefinir a senha com o token"""
    return email_service.reset_password(request)
