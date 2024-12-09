from flask import Blueprint, request
from services.activity_service import ActivityService

bp_activity = Blueprint("activity", __name__, url_prefix="/activity")


@bp_activity.route("/initialize", methods=["POST"])
def initialize_activity():
    return ActivityService.initialize_activity(request)


@bp_activity.route("/publish/<int:id_activity>", methods=["PUT"])
def publish_activity(id_activity):
    return ActivityService.publish_activity(id_activity)


@bp_activity.route("/findById/<int:id_activity>", methods=["GET"])
def get_activity_by_id(id_activity):
    return ActivityService.get_activity_by_id(id_activity)


@bp_activity.route("/findByStudentId/<int:id_student>", methods=["GET"])
def get_activity_by_student_id(id_student):
    return ActivityService.get_activities_by_student_id(id_student)


@bp_activity.route("/update/<int:id_activity>", methods=["PUT"])
def update_activity(id_activity):
    title = request.get_json()["title"]
    return ActivityService.update_activity(id_activity, title)


@bp_activity.route("/delete/<int:id_activity>", methods=["DELETE"])
def delete_activity(id_activity):
    return ActivityService.delete_activity(id_activity)
