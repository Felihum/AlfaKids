from flask import Request, jsonify
from db import database
from models.subject.subject import Subject


class SubjectService:
    @staticmethod
    def create_subject(request: Request):
        request_subject: Subject = request.get_json()

        name: str = request_subject["name"]

        if not name:
            return jsonify({"error": "Some field(s) has no value."}), 400

        new_subject: Subject = Subject(name)
        database.session.add(new_subject)
        database.session.commit()

        return jsonify({"message": "Subject registered successfully!",
                        "subject": new_subject.to_dict()}), 201

    @staticmethod
    def get_all_subjects():
        subjects: Subject = Subject.query.all()

        if not subjects:
            return jsonify({"error": "There are no subjects."}), 404

        subjects_dict_list = [subject.to_dict() for subject in subjects]

        return jsonify({"message": "Subjects found",
                        "subjects": subjects_dict_list}), 200

    @staticmethod
    def get_subject_by_id(id_subject):
        subject: Subject = Subject.query.get(id_subject)

        if not subject:
            return jsonify({"error": "Subject not found"}), 404

        return jsonify({"message": "Subject found",
                        "subject": subject.to_dict()}), 200

    @staticmethod
    def get_subject_by_name(name):
        subject: Subject = Subject.query.filter_by(name=name).first()

        if not subject:
            return jsonify({"error": "Subject not found"}), 404

        return jsonify({"message": "Subject found",
                        "subject": subject.to_dict()}), 200

    @staticmethod
    def update_subject(id_subject, request: Request):
        subject: Subject = Subject.query.get(id_subject)

        if not subject:
            return jsonify({"error": "Subject not found"}), 404

        request_subject = request.get_json()

        name: str = request_subject["name"]

        if not name:
            return jsonify({"error": "Some field(s) has no value."}), 400

        subject.name = name

        database.session.commit()

        return jsonify({"message": "Subject updated successfully!",
                        "subject": subject.to_dict()}), 200

    @staticmethod
    def delete_subject(id_subject):
        subject: Subject = Subject.query.get(id_subject)

        if not subject:
            return jsonify({"error": "Subject not found"}), 404

        database.session.delete(subject)
        database.session.commit()

        return jsonify({"message": "Subject deleted successfully!"}), 200
