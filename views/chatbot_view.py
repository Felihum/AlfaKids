from flask import Blueprint, request, jsonify
import requests

bp_chatbot = Blueprint("chatbot", __name__, url_prefix="/chatbot")

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@bp_chatbot.route("/message", methods=["POST"])
def chatbot_message():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        sender_id = data.get("sender", "default")

        # Enviar a mensagem para o chatbot Rasa
        response = requests.post(RASA_URL, json={"sender": sender_id, "message": user_message})

        if response.status_code == 200:
            return jsonify({"response": response.json()}), 200
        else:
            return jsonify({"error": "Erro ao comunicar com o chatbot."}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
