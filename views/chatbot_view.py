from flask import Blueprint, request, jsonify
from services.chatbot_service import ChatbotService

bp_chatbot = Blueprint("chatbot", __name__, url_prefix="/chatbot")

@bp_chatbot.route("/message", methods=["POST"])
def chatbot_message():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        sender_id = data.get("sender", "default")

        response, status_code = ChatbotService.send_message_to_rasa(user_message, sender_id)

        return jsonify(response), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500
