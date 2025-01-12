from flask import Blueprint, request
from services.student_accomplishment_service import StudentAccomplishmentService

bp_accomplishment = Blueprint("accomplishment", __name__, url_prefix="/accomplishment")


@bp_accomplishment.route("/register", methods=["POST"])
def accomplish_activity():
    return StudentAccomplishmentService.accomplish_activity(request)


@bp_accomplishment.route("/findStudentsByActivityId/<int:id_activity>", methods=["GET"])
def get_all_students_by_activity_id(id_activity):
    return StudentAccomplishmentService.get_all_students_by_activity_id(id_activity)


@bp_accomplishment.route("/findActivitiesByStudentId/<int:id_student>", methods=["GET"])
def get_all_activities_by_student_id(id_student):
    return StudentAccomplishmentService.get_all_activities_by_student_id(id_student)


@bp_accomplishment.route("/delete/<int:id_activity>/<int:id_student>", methods=["DELETE"])
def delete_accomplishment(id_activity, id_student):
    return StudentAccomplishmentService.delete_accomplishment(id_activity, id_student)
