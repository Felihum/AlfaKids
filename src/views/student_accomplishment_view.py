from flask import Blueprint, request
from src.services.student_accomplishment_service import StudentAccomplishmentService

bp_accomplishment = Blueprint("accomplishment", __name__, url_prefix="/accomplishment")


@bp_accomplishment.route("/register", methods=["POST"])
def accomplish_activity():
    return StudentAccomplishmentService.accomplish_activity(request)


@bp_accomplishment.route("/findStudentsByActivityId/<string:id_activity>", methods=["GET"])
def get_all_students_by_activity_id(id_activity):
    return StudentAccomplishmentService.get_all_students_by_activity_id(id_activity)


@bp_accomplishment.route("/findActivitiesByStudentId/<string:id_student>", methods=["GET"])
def get_all_activities_by_student_id(id_student):
    return StudentAccomplishmentService.get_all_activities_by_student_id(id_student)


@bp_accomplishment.route("/delete/<string:id_activity>/<string:id_student>", methods=["DELETE"])
def delete_accomplishment(id_activity, id_student):
    return StudentAccomplishmentService.delete_accomplishment(id_activity, id_student)
