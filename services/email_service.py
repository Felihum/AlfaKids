from flask import Request, jsonify
from flask_mail import Message
from mail import mail

import config


class EmailService:

    @staticmethod
    def submit(request: Request):
        try:
            #request_submit_email = request.get_json()

            #email:str = request_submit_email.get("email")

            #if not email:
            #    return jsonify({"message": "Email not provided"}), 400

            msg = Message(subject="Recuperação de Senha",
                          sender="alfakids.app@gmail.com",
                          recipients=["nucap.games@gmail.com"])
            msg.body = "Acesse o seguinte link para redefinir sua senha."
            print(msg)
            mail.send(msg)
            return jsonify({"message": "Email sent successfully!"}), 200
        except Exception as ex:
            print(f"An exception occurred: {ex}")
            return jsonify({"message": "Failed to send email."}), 500