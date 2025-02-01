import requests
from flask import jsonify

RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'


class ChatbotService:
    @staticmethod
    def send_message_to_rasa(message, sender_id="user"):
        """Envia uma mensagem para o Rasa e retorna a resposta."""
        try:
            response = requests.post(RASA_URL, json={'sender': sender_id, 'message': message})
            rasa_response = response.json()

            if rasa_response:
                # Retorna a resposta do chatbot
                return jsonify({'response': rasa_response[0].get('text', 'Não entendi sua mensagem.')})
            else:
                return jsonify({'response': 'Desculpe, houve um erro ao processar sua mensagem.'})

        except Exception as e:
            return jsonify({'error': str(e)}), 500
