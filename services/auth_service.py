from flask import Request, jsonify
from models.student.student import Student
from flask_jwt_extended import create_access_token
from models.professor.professor import Professor
import bcrypt

class AuthService:

    @staticmethod
    def login_student(request: Request):
        email: str = request.get_json()["email"]
        password: str = request.get_json()["password"]

        student: Student = Student.query.filter_by(email=email).first()

        if not student:
            return jsonify({"error": "Invalid Credentials"}), 401

        # Verificando a senha usando bcrypt
        if not bcrypt.checkpw(password.encode('utf-8'), student.password.encode('utf-8')):
            return jsonify({"error": "Invalid Credentials"}), 401

        # Gerando o token JWT para o professor
        access_token = create_access_token(identity={"id": student.id})

        return jsonify({"token": access_token}), 200

    @staticmethod
    def login_professor(request: Request):
        email: str = request.get_json()["email"]
        password: str = request.get_json()["password"]

        professor: Professor = Professor.query.filter_by(email=email).first()

        if not professor:
            return jsonify({"error": "Invalid Credentials"}), 401

        # Verificando a senha usando bcrypt
        if not bcrypt.checkpw(password.encode('utf-8'), professor.password.encode('utf-8')):
            return jsonify({"error": "Invalid Credentials"}), 401

        # Gerando o token JWT para o professor
        access_token = create_access_token(identity={"id": professor.id})

        return jsonify({"token": access_token}), 200
