from flask import Request, jsonify
from src.db import database
from src.models.student_accomplishment.student_accomplishment import StudentAccomplishment
from src.services.student_service import StudentService
from src.services.activity_service import ActivityService
from src.models.student.student import Student
from src.models.activity.activity import Activity


class StudentAccomplishmentService:
    @staticmethod
    def accomplish_activity(request: Request):
        request_accomplishment: StudentAccomplishment = request.get_json()

        id_activity = request_accomplishment["id_activity"]
        id_student = request_accomplishment["id_student"]

        if not id_activity or not id_student:
            return jsonify({"error": "Some field(s) has no value."}), 400

        if not StudentAccomplishmentService.verify_existence_of_activity_id(id_activity):
            return jsonify({"error": "There is no activity."}), 404

        if not StudentAccomplishmentService.verify_existence_of_student_id(id_student):
            return jsonify({"error": "There is no student."}), 404

        new_accomplishment: StudentAccomplishment = StudentAccomplishment(id_activity, id_student)

        database.session.add(new_accomplishment)
        database.session.commit()

        return jsonify({"message": "Accomplishment registered successfully!",
                        "accomplishment": new_accomplishment.to_dict()}), 201

    @staticmethod
    def get_all_students_by_activity_id(id_activity):
        accomplishments = StudentAccomplishment.query.filter_by(id_activity=id_activity).all()
        students: list[Student] = list()

        if not accomplishments:
            return jsonify({"error": "There are no accomplishments."}), 404

        for accomplishment in accomplishments:
            student: Student = Student.query.get(accomplishment.id_student)

            students.append(student)

        students_dict_list = [student.to_dict() for student in students]

        return jsonify({"message": "Students found",
                        "students": students_dict_list}), 200

    @staticmethod
    def get_all_activities_by_student_id(id_student):
        accomplishments = StudentAccomplishment.query.filter_by(id_student=id_student).all()
        activities = list()

        if not accomplishments:
            return jsonify({"error": "There are no accomplishments."}), 404

        for accomplishment in accomplishments:
            activity: Activity = Activity.query.get(accomplishment.id_activity)

            activities.append(activity)

        activities_dict_list = [activity.to_dict() for activity in activities]

        return jsonify({"message": "Activities found",
                        "activities": activities_dict_list}), 200

    @staticmethod
    def delete_accomplishment(id_activity, id_student):
        accomplishment: StudentAccomplishment = StudentAccomplishment.query.filter_by(id_activity=id_activity, id_student=id_student).first()

        if not accomplishment:
            return jsonify({"error": "There is no accomplishment."}), 404

        database.session.delete(accomplishment)
        database.session.commit()

        return jsonify({"message": "Accomplishment deleted successfully!"}), 200

    @staticmethod
    def verify_existence_of_student_id(id_student):
        student: Student = StudentService.get_student_by_id(id_student)

        if not student:
            return False

        return True

    @staticmethod
    def verify_existence_of_activity_id(id_activity):
        activity: Activity = ActivityService.get_activity_by_id(id_activity)

        if not activity:
            return False

        return True
