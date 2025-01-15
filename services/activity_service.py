from flask import Request, jsonify
from db import database
from models.activity.activity_status import ActivityStatus
from models.activity.activity import Activity
from models.classroom.classroom import Classroom
from models.activity_distribution.activity_distribution import ActivityDistribution
from models.question.question import Question
from models.student_accomplishment.student_accomplishment import StudentAccomplishment
from models.student_answer.student_answer import StudentAnswer


class ActivityService:

    @staticmethod
    def initialize_activity(request: Request):
        activity_request = request.get_json()

        title: str = activity_request["title"]
        status: str = ActivityStatus.INITIALIZED.name
        id_subject: int = activity_request["id_subject"]
        id_professor: int = activity_request["id_professor"]

        if not title or not status or not id_subject or not id_professor:
            return jsonify({"error": "Some field is missing!"}), 400

        activity: Activity = Activity(title, status, id_subject, id_professor)

        database.session.add(activity)
        database.session.commit()

        return jsonify({"message": "Activity initialized successfully!",
                        "activity": activity.to_dict()}), 201

    @staticmethod
    def distribute_activity(request: Request):
        distribution_request = request.get_json()

        id_classroom: int = distribution_request["id_classroom"]
        id_activity: int = distribution_request["id_activity"]

        classroom: Classroom = Classroom.query.get(id_classroom)
        activity: Activity = Activity.query.get(id_activity)

        existing_distribution = ActivityDistribution.query.filter_by(id_activity=id_activity, id_classroom=id_classroom).first()

        if existing_distribution:
            return jsonify({"error": "Activity already distributed in this classroom!"}), 500

        if activity.status != ActivityStatus.PUBLISHED.name:
            activity.status = ActivityStatus.PUBLISHED.name

        if not activity:
            return jsonify({"error": "Activity not found!"}), 404

        if not classroom:
            return jsonify({"error": "Classroom not found!"}), 404

        if not id_classroom or not id_activity:
            return jsonify({"error": "Some field is missing!"})

        distribution: ActivityDistribution = ActivityDistribution(id_activity, id_classroom)

        database.session.add(distribution)
        database.session.commit()

        return jsonify({"message": "Distribution created successfully!",
                        "distribution": distribution.to_dict()})

    @staticmethod
    def get_activity_by_id(id_activity):
        activity: Activity = Activity.query.get(id_activity)

        if not activity:
            return jsonify({"error": "Activity not found"}), 404

        return jsonify({"message": "Activity found",
                        "activity": activity.to_dict()}), 200

    @staticmethod
    def get_activities_by_professor_id(id_professor):
        activities = Activity.query.filter_by(id_professor=id_professor).all()

        if not activities:
            return jsonify({"error": "There are no activities!"}), 404

        activities_dict_list = [activity.to_dict() for activity in activities]

        return jsonify({"message": "Activities found",
                        "activities": activities_dict_list}), 200

    @staticmethod
    def get_all_accomplished_activities(id_student):
        accomplishments = StudentAccomplishment.query.filter_by(id_student=id_student).all()
        activities = list()

        for accomplishment in accomplishments:
            activity: Activity = Activity.query.get(accomplishment.id_activity)

            if activity:
                activities.append(activity)

        if not activities:
            return jsonify({"error": "There are no accomplished activities!"}), 404

        activities_dict_list = [activity.to_dict() for activity in activities]

        return jsonify({"message": "Activities found",
                        "activities": activities_dict_list}), 200

    @staticmethod
    def get_all_unaccomplished_activities(id_classroom, id_student):
        activity_distributions = ActivityDistribution.query.filter_by(id_classroom=id_classroom).all()
        activities = list()

        if not activity_distributions:
            return jsonify({"error": "There are no activities in this classroom!"}), 404

        for activity_distribution in activity_distributions:
            activities.append(Activity.query.get(activity_distribution.id_activity))

        unaccomplished_activities = [
            activity for activity in activities
            if not StudentAccomplishment.query.filter_by(id_activity=activity.id, id_student=id_student).first()
        ]

        if not unaccomplished_activities:
            return jsonify({"error": "There are no activities!"}), 404

        activities_dict_list = [activity.to_dict() for activity in unaccomplished_activities]

        return jsonify({"message": "Activities found",
                        "activities": activities_dict_list}), 200

    @staticmethod
    def get_activities_by_classroom_id(id_classroom):
        activity_distributions = ActivityDistribution.query.filter_by(id_classroom=id_classroom).all()
        activities = list()

        if not activity_distributions:
            return jsonify({"error": "There are no activities in this classroom!"}), 404

        for activity_distribution in activity_distributions:
            activities.append(Activity.query.get(activity_distribution.id_activity))

        activities_dict_list = [activity.to_dict() for activity in activities]

        return jsonify({"message": "Activity found",
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
    def update_activity_title(id_activity, title):
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

        activity_distributions = ActivityDistribution.query.filter_by(id_activity=id_activity).all()
        activity_questions = Question.query.filter_by(id_activity=id_activity).all()
        activity_accomplishments = StudentAccomplishment.query.filter_by(id_activity=id_activity).all()
        activity_answers = StudentAnswer.query.filter_by(id_activity=id_activity).all()

        if activity_distributions:
            for activity_distribution in activity_distributions:
                database.session.delete(activity_distribution)
                database.session.commit()

        if activity_accomplishments:
            for activity_accomplishment in activity_accomplishments:
                database.session.delete(activity_accomplishment)
                database.session.commit()

        if activity_answers:
            for activity_answer in activity_answers:
                database.session.delete(activity_answer)
                database.session.commit()

        if activity_questions:
            for activity_question in activity_questions:
                database.session.delete(activity_question)
                database.session.commit()

        database.session.delete(activity)
        database.session.commit()

        return jsonify({"message": "Activity deleted successfully!"}), 200
