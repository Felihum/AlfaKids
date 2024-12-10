from flask import Blueprint, request
from services.classroom_service import ClassroomService

bp_classroom = Blueprint("classroom", __name__, url_prefix="/classroom")


@bp_classroom.route("/initialize", methods=["POST"])
def initialize_classroom():
    return ClassroomService.initialize_classroom(request)


@bp_classroom.route("/fulfill/<int:id_classroom>", methods=["PUT"])
def fulfill_classroom(id_classroom):
    return ClassroomService.fulfill_classroom(id_classroom)


@bp_classroom.route("/findById/<int:id_classroom>", methods=["GET"])
def get_classroom_by_id(id_classroom):
    return ClassroomService.get_classroom_by_id(id_classroom)


@bp_classroom.route("/allocateStudentInClassroom", methods=["POST"])
def allocate_student_in_classroom():
    return ClassroomService.allocate_student_in_classroom(request)


@bp_classroom.route("/findByNumberAndYear/<int:number>/<int:year>", methods=["GET"])
def get_classroom_by_number_and_year(number: int, year: int):
    return ClassroomService.get_classroom_by_number_and_year(number, year)


@bp_classroom.route("/findByStudentId/<int:id_student>", methods=["GET"])
def get_classrooms_by_student_id(id_student: int):
    return ClassroomService.get_classrooms_by_student_id(id_student)


@bp_classroom.route("/close/<int:id_classroom>", methods=["PUT"])
def close_classroom(id_classroom: int):
    return ClassroomService.close_classroom(id_classroom)


@bp_classroom.route("/updateProfessor/<int:id_classroom>", methods=["PUT"])
def update_classroom_professor(id_classroom: int):
    return ClassroomService.update_classroom_professor(id_classroom, request)


@bp_classroom.route("/delete/<int:id_classroom>", methods=["DELETE"])
def delete_classroom(id_classroom: int):
    return ClassroomService.delete_classroom(id_classroom)
