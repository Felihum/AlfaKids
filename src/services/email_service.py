import requests
from flask import jsonify, Request

EMAIL_URL = "http://email:5050/submit"

class EmailService:

    @staticmethod
    def submit(request: Request):
        data = request.get_json()

        recipient = data.get("recipient")

        try:
            response = requests.post(EMAIL_URL, json={"recipient": recipient})

            # Verifica o status da resposta
            if response.status_code != 200:
                print(f" Erro ao comunicar com o serviço: {response.status_code}")
                return jsonify({"error": "Erro ao se comunicar com o serviço"}), 500

            return jsonify({"message": "Email enviado com sucesso!"}), 200

        except Exception as e:
            # Erro genérico
            print(f" Erro interno no backend: {str(e)}")
            return jsonify({"error": f"Erro interno no serviço: {str(e)}"}), 500
