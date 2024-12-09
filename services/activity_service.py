from flask import Request, jsonify
from db import database
from models.activity.activity_status import ActivityStatus
from models.activity.activity import Activity


class ActivityService:

    @staticmethod
    def initialize_activity(request: Request):
        activity_request = request.get_json()

        title: str = activity_request["title"]
        status: str = ActivityStatus.INITIALIZED.name
        id_subject: int = activity_request["id_subject"]
        id_student: int = activity_request["id_student"]

        if not title or not status or not id_subject or not id_student:
            return jsonify({"error": "Some field is missing!"})

        activity: Activity = Activity(title, status, id_subject, id_student)

        database.session.add(activity)
        database.session.commit()

        return jsonify({"message": "Activity initialized successfully!",
                        "activity": activity.to_dict()})

    @staticmethod
    def get_activity_by_id(id_activity):
        activity: Activity = Activity.query.get(id_activity)

        if not activity:
            return jsonify({"error": "Activity not found"}), 404

        return jsonify({"message": "Activity found",
                        "activity": activity.to_dict()}), 200

    @staticmethod
    def get_activities_by_student_id(id_student):
        activities = Activity.query.filter_by(id_student=id_student).all()

        if not activities:
            return jsonify({"error": "There are no accountables!"}), 404

        activities_dict_list = [activity.to_dict() for activity in activities]

        return jsonify({"message": "Activities found",
                        "activities": activities_dict_list}), 200

    @staticmethod
    def publish_activity(id_activity):
        activity: Activity = Activity.query.get(id_activity)

        if not activity:
            return jsonify({"error": "Activity not found"}), 404

        activity.status = ActivityStatus.PUBLISHED.name

        database.session.commit()

        return jsonify({"message": "Activity published successfully",
                        "activity": activity.to_dict()}), 200

    @staticmethod
    def update_activity(id_activity, title):
        activity: Activity = Activity.query.get(id_activity)

        if not activity:
            return jsonify({"error": "Activity not found"}), 404

        activity.title = title

        database.session.commit()

        return jsonify({"message": "Activity updated successfully",
                        "activity": activity.to_dict()}), 200

    @staticmethod
    def delete_activity(id_activity):
        activity: Activity = Activity.query.get(id_activity)

        if not activity:
            return jsonify({"error": "Activity not found"}), 404

        database.session.delete(activity)
        database.session.commit()

        return jsonify({"message": "Activity deleted successfully!"}), 200

