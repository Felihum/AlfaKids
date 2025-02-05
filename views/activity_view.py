from flask import request, Blueprint
from services.activity_service import ActivityService

bp_activity = Blueprint("activity", __name__, url_prefix="/activity")


@bp_activity.route("/initialize", methods=["POST"])
def initialize_activity():
    return ActivityService.initialize_activity(request)


@bp_activity.route("/distribute", methods=["POST"])
def distribute_activity():
    return ActivityService.distribute_activity(request)


@bp_activity.route("/publish/<string:id_activity>", methods=["PUT"])
def publish_activity(id_activity):
    return ActivityService.publish_activity(id_activity)


@bp_activity.route("/findById/<string:id_activity>", methods=["GET"])
def get_activity_by_id(id_activity):
    return ActivityService.get_activity_by_id(id_activity)


@bp_activity.route("/findAllUnaccomplished/<string:id_classroom>/<string:id_student>", methods=["GET"])
def get_all_unaccomplished_activities(id_classroom, id_student):
    return ActivityService.get_all_unaccomplished_activities(id_classroom, id_student)


@bp_activity.route("/findAllAccomplished/<string:id_student>", methods=["GET"])
def get_all_accomplished_activities(id_student):
    return ActivityService.get_all_accomplished_activities(id_student)


@bp_activity.route("/findByClassroomId/<string:id_classroom>", methods=["GET"])
def get_activity_by_classroom_id(id_classroom):
    return ActivityService.get_activities_by_classroom_id(id_classroom)


@bp_activity.route("/findByProfessorId/<string:id_professor>", methods=["GET"])
def get_activity_by_professor_id(id_professor):
    return ActivityService.get_activities_by_professor_id(id_professor)


@bp_activity.route("/updateTitle/<string:id_activity>", methods=["PUT"])
def update_activity(id_activity):
    title = request.get_json()["title"]
    return ActivityService.update_activity_title(id_activity, title)


@bp_activity.route("/delete/<string:id_activity>", methods=["DELETE"])
def delete_activity(id_activity):
    return ActivityService.delete_activity(id_activity)
