from flask import Request, jsonify
from src.models.accountable.accountable import Accountable
from src.db import database
from src.services.student_service import StudentService


class AccountableService:

    @staticmethod
    def create_accountable(request: Request):
        request_accountable: Accountable = request.get_json()

        name: str = request_accountable["name"]
        email: str = request_accountable["email"]
        telephone: str = request_accountable["telephone"]
        id_student = request_accountable["id_student"]

        if not name or not email or not telephone or not id_student:
            return jsonify({"error": "Some field(s) has no value."}), 400

        if not StudentService.get_student_by_id(id_student):
            return jsonify({"error": "Student not found!"}), 404

        new_accountable: Accountable = Accountable(name, email, telephone, id_student)
        database.session.add(new_accountable)
        database.session.commit()

        return jsonify({"message": "Accountable registered successfully!",
                        "accountable": new_accountable.to_dict()}), 201

    @staticmethod
    def get_accountable_by_id(id_accountable):
        accountable: Accountable = Accountable.query.get(id_accountable)

        if not accountable:
            return jsonify({"error": "Accountable not found"}), 404

        return jsonify({"message": "Accountable found",
                        "accountable": accountable.to_dict()}), 200

    @staticmethod
    def get_accountables_by_student_id(id_student):
        accountables = Accountable.query.filter_by(id_student=id_student).all()

        if not accountables:
            return jsonify({"error": "There are no accountables!"}), 404

        accountables_dict_list = [accountable.to_dict() for accountable in accountables]

        return jsonify({"message": "Accountables found",
                        "accountables": accountables_dict_list}), 200

    @staticmethod
    def get_accountable_by_email(email):
        accountable: Accountable = Accountable.query.filter_by(email=email).first()

        if not accountable:
            return jsonify({"error": "Accountable not found"}), 404

        return jsonify({"message": "Accountable found",
                        "accountable": accountable.to_dict()}), 200

    @staticmethod
    def update_accountable(id_student, request: Request):
        accountable: Accountable = Accountable.query.get(id_student)

        if not accountable:
            return jsonify({"error": "Accountable not found"}), 404

        request_accountable = request.get_json()

        name: str = request_accountable["name"]
        email: str = request_accountable["email"]
        password: str = request_accountable["password"]

        if not name or not email or not password or not id_student:
            return jsonify({"error": "Some field(s) has no value."}), 400

        accountable.name = name
        accountable.email = email
        accountable.password = password

        database.session.commit()

        return jsonify({"message": "Accountable updated successfully!",
                        "accountable": accountable.to_dict()}), 200

    @staticmethod
    def delete_accountable(id_accountable):
        accountable: Accountable = Accountable.query.get(id_accountable)

        if not accountable:
            return jsonify({"error": "Accountable not found"}), 404

        database.session.delete(accountable)
        database.session.commit()

        return jsonify({"message": "Accountable deleted successfully!"}), 200
