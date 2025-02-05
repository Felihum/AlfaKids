from flask import Blueprint, request
from services.classroom_service import ClassroomService

bp_classroom = Blueprint("classroom", __name__, url_prefix="/classroom")


@bp_classroom.route("/initialize", methods=["POST"])
def initialize_classroom():
    return ClassroomService.initialize_classroom(request)


@bp_classroom.route("/fulfill/<string:id_classroom>", methods=["PUT"])
def fulfill_classroom(id_classroom):
    return ClassroomService.fulfill_classroom(id_classroom)


@bp_classroom.route("/findById/<string:id_classroom>", methods=["GET"])
def get_classroom_by_id(id_classroom):
    return ClassroomService.get_classroom_by_id(id_classroom)


@bp_classroom.route("/allocateStudentInClassroom", methods=["POST"])
def allocate_student_in_classroom():
    return ClassroomService.allocate_student_in_classroom(request)


@bp_classroom.route("/findByNumberAndYear/<int:number>/<int:year>", methods=["GET"])
def get_classroom_by_number_and_year(number: int, year: int):
    return ClassroomService.get_classroom_by_number_and_year(number, year)


@bp_classroom.route("/findByStudentId/<string:id_student>", methods=["GET"])
def get_classrooms_by_student_id(id_student: int):
    return ClassroomService.get_classrooms_by_student_id(id_student)


@bp_classroom.route("/findByActivityId/<string:id_activity>", methods=["GET"])
def get_classrooms_by_activity_id(id_activity: int):
    return ClassroomService.get_classrooms_by_activity_id(id_activity)


@bp_classroom.route("/findClassroomsToDistribute/<string:id_activity>/<string:id_professor>", methods=["GET"])
def get_classrooms_to_distribute(id_activity: int, id_professor: int):
    return ClassroomService.get_classrooms_to_distribute(id_activity, id_professor)



@bp_classroom.route("/findByProfessorId/<string:id_professor>", methods=["GET"])
def get_classrooms_by_professor_id(id_professor: int):
    return ClassroomService.get_classrooms_by_professor_id(id_professor)


@bp_classroom.route("/close/<string:id_classroom>", methods=["PUT"])
def close_classroom(id_classroom: int):
    return ClassroomService.close_classroom(id_classroom)


@bp_classroom.route("/updateProfessor/<string:id_classroom>", methods=["PUT"])
def update_classroom_professor(id_classroom: int):
    return ClassroomService.update_classroom_professor(id_classroom, request)


@bp_classroom.route("/delete/<string:id_classroom>", methods=["DELETE"])
def delete_classroom(id_classroom: int):
    return ClassroomService.delete_classroom(id_classroom)


@bp_classroom.route("/deleteStudentFromClassroom/<string:id_classroom>/<string:id_student>", methods=["DELETE"])
def delete_student_from_classroom(id_classroom: int, id_student: int):
    return ClassroomService.delete_student_from_classroom(id_classroom, id_student)
