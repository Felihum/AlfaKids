from flask import Blueprint, request
from services.student_service import StudentService

bp_student = Blueprint("student", __name__, url_prefix="/student")

__student_service = StudentService()

@bp_student.route("/register", methods=["POST"])
def create_student():
    return __student_service.create_student(request)


@bp_student.route("/findById/<int:id_student>", methods=["GET"])
def get_student_by_id(id_student):
    return __student_service.get_student_by_id(id_student)


@bp_student.route("/findByEmail/<string:email>", methods=["GET"])
def get_student_by_email(email):
    return __student_service.get_student_by_email(email)


@bp_student.route("/update/<int:id_student>", methods=["PUT"])
def update_student(id_student):
    return __student_service.update_student(id_student, request)


@bp_student.route("/delete/<int:id_student>", methods=["DELETE"])
def delete_student(id_student):
    return __student_service.delete_student(id_student)
