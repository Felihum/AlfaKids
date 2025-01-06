from flask import Request, jsonify
from models.student.student import Student
from flask_jwt_extended import create_access_token


class AuthService:

    @staticmethod
    def login(request: Request):
        email: str = request.get_json()["email"]
        password: str = request.get_json()["password"]

        student: Student = Student.query.filter_by(email=email).first()

        if not student:
            return jsonify({"error": "Invalid Credentials"}), 401

        if student.password != password:
            return jsonify({"error": "Invalid Credentials"}), 401

        access_token = create_access_token(identity={"id": student.id})

        return jsonify({"token": access_token}), 200
