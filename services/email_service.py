from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from flask import current_app, Request, jsonify
from models.student.student import Student
from db import database
import bcrypt


class EmailService:

    # Inicializa o Mail
    mail = Mail()

    def init_email_service(self, app):
        self.mail.init_app(app)

    def generate_reset_token(self, email):
        """Gera um token para recuperação de senha."""
        s = URLSafeTimedSerializer(current_app.secret_key)
        return s.dumps(email, salt='password-reset-salt')

    def request_reset(self, request: Request):
        email = request.get_json()['email']
        student: Student = Student.query.filter_by(email=email).first()
        if student:
            token = self.generate_reset_token(email)

            """Envia um e-mail com o link de recuperação de senha."""
            link = f"http://localhost:5173/forgot/reset/{token}"  # Altere para o URL do seu frontend
            msg = Message('Recuperação de Senha',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=[email])
            msg.body = f'Clique no link para redefinir sua senha: {link}'
            self.mail.send(msg)

            return jsonify({'message': 'E-mail enviado! Verifique sua caixa de entrada.'}), 200

        return jsonify({'error': 'E-mail não encontrado.'}), 404

    def reset_password(self, request: Request):
        token = request.get_json()['token']
        email = self.verify_reset_token(token)
        if email is None:
            return jsonify({'error': 'Token inválido ou expirado.'}), 400

        student: Student = Student.query.filter_by(email=email).first()
        new_password = request.json.get('password')

        if not new_password:
            return jsonify({'error': 'A nova senha não foi fornecida.'}), 400

        # Criptografar a nova senha antes de salvar
        student.password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        database.session.commit()

        return jsonify({'message': 'Senha redefinida com sucesso!'}), 200

    def verify_reset_token(self, token):
        """Verifica se o token é válido e retorna o e-mail associado."""
        s = URLSafeTimedSerializer(current_app.secret_key)
        try:
            email = s.loads(token, salt='password-reset-salt', max_age=3600)  # O token expira em 1 hora
            return email
        except (SignatureExpired, BadSignature):
            return None