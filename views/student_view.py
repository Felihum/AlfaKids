from flask import Blueprint, request
from services.student_service import StudentService

bp_student = Blueprint("student", __name__, url_prefix="/student")


@bp_student.route("/register", methods=["POST"])
def create_student():
    return StudentService.create_student(request)


@bp_student.route("/findById/<string:id_student>", methods=["GET"])
def get_student_by_id(id_student):
    return StudentService.get_student_by_id(id_student)


@bp_student.route("/findAll", methods=["GET"])
def get_all_students():
    return StudentService.get_all_students()


@bp_student.route("/findByClassroomId/<string:id_classroom>", methods=["GET"])
def get_students_by_classroom_id(id_classroom):
    return StudentService.get_students_by_classroom_id(id_classroom)


@bp_student.route("/findByEmail/<string:email>", methods=["GET"])
def get_student_by_email(email):
    return StudentService.get_student_by_email(email)


@bp_student.route("/filterByEmail/<string:email>", methods=["GET"])
def filter_students_by_email(email):
    return StudentService.filter_students_by_email(email)


@bp_student.route("/update/<string:id_student>", methods=["PUT"])
def update_student(id_student):
    return StudentService.update_student(id_student, request)


@bp_student.route("/update/password/<string:email>", methods=["PUT"])
def update_password(email):
    return StudentService.update_password(email, request)


@bp_student.route("/delete/<string:id_student>", methods=["DELETE"])
def delete_student(id_student):
    return StudentService.delete_student(id_student)
