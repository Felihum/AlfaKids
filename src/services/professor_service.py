from flask import Request, jsonify
from src.models.professor.professor import Professor
from src.db import database
import bcrypt

class ProfessorService:
    @staticmethod
    def create_professor(request: Request):
        request_professor: Professor = request.get_json()

        name: str = request_professor["name"]
        email: str = request_professor["email"]
        password: str = request_professor["password"]
        registration: int = request_professor["registration"]

        if not name or not email or not password or not registration:
            return jsonify({"error": "Some field(s) has no value."}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) # Encripted Password

        new_professor: Professor = Professor(name, email, hashed_password.decode('utf-8'), registration)
        database.session.add(new_professor)
        database.session.commit()

        return jsonify({"message": "Professor registered successfully!",
                        "professor": new_professor.to_dict()}), 201

    @staticmethod
    def get_professor_by_id(id_professor):
        professor: Professor = Professor.query.get(id_professor)

        if not professor:
            return jsonify({"error": "Professor not found"}), 404

        return jsonify({"message": "Professor found",
                        "professor": professor.to_dict()}), 200

    @staticmethod
    def get_professor_by_email(email):
        professor: Professor = Professor.query.filter_by(email=email).first()

        if not professor:
            return jsonify({"error": "Professor not found"}), 404

        return jsonify({"message": "Professor found",
                        "professor": professor.to_dict()}), 200

    @staticmethod
    def update_professor(id_professor, request: Request):
        professor: Professor = Professor.query.get(id_professor)

        if not professor:
            return jsonify({"error": "Professor not found"}), 404

        request_professor = request.get_json()

        name: str = request_professor["name"]
        email: str = request_professor["email"]
        password: str = request_professor["password"]
        registration: int = request_professor["registration"]

        if not name or not email or not password or not registration:
            return jsonify({"error": "Some field(s) has no value."}), 400

        professor.name = name
        professor.email = email
        professor.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        professor.registration = registration

        database.session.commit()

        return jsonify({"message": "Professor updated successfully!",
                        "professor": professor.to_dict()}), 200

    @staticmethod
    def delete_professor(id_professor):
        professor: Professor = Professor.query.get(id_professor)

        if not professor:
            return jsonify({"error": "Professor not found"}), 404

        database.session.delete(professor)
        database.session.commit()

        return jsonify({"message": "Professor deleted successfully!"}), 200
