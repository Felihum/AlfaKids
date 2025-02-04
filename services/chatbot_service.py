import requests
from flask import jsonify

RASA_URL = "http://chatbot:5005/webhooks/rest/webhook"

class ChatbotService:
    @staticmethod
    def send_message_to_rasa(message, sender_id="user"):
        try:
            # Exibe a mensagem enviada ao Rasa
            print(f"🔧 Enviando para o Rasa: {message}")

            # Envia a mensagem para o Rasa
            response = requests.post(RASA_URL, json={"sender": sender_id, "message": message})

            # Verifica o status da resposta
            if response.status_code != 200:
                print(f" Erro ao comunicar com o Rasa: {response.status_code}")
                return jsonify({"error": "Erro ao se comunicar com o Rasa"}), 500

            # Exibe a resposta bruta do Rasa
            try:
                rasa_response = response.json()
                print(rasa_response[0]["recipient_id"])
                print(" Resposta do Rasa:", rasa_response[0])  # Exibe a resposta do Rasa
            except ValueError as e:
                # Caso o conteúdo não seja um JSON válido
                print(" Erro ao processar a resposta JSON:", e)
                return jsonify({"error": "Erro ao processar a resposta do Rasa"}), 500

            # Verifica se a resposta do Rasa é válida (uma lista)
            if rasa_response and isinstance(rasa_response, list):
                # Retorna a resposta do Rasa em formato JSON
                return jsonify({"message": "Rasa response!",
                                "response": rasa_response[0]}), 200
            else:
                # Caso a resposta não seja uma lista válida
                print(" Resposta inválida do Rasa:", rasa_response)
                return jsonify([]), 200  # Retorna uma lista vazia caso a resposta seja inválida

        except requests.exceptions.RequestException as req_err:
            # Erro ao se comunicar com o Rasa
            print(f" Erro ao conectar ao Rasa: {str(req_err)}")
            return jsonify({"error": f"Erro ao conectar ao Rasa: {str(req_err)}"}), 500

        except Exception as e:
            # Erro genérico
            print(f" Erro interno no backend: {str(e)}")
            return jsonify({"error": f"Erro interno no chatbot: {str(e)}"}), 500
