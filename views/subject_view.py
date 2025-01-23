from flask import Blueprint, request
from services.subject_service import SubjectService

bp_subject = Blueprint("subject", __name__, url_prefix="/subject")


@bp_subject.route("/register", methods=["POST"])
def create_subject():
    return SubjectService.create_subject(request)


@bp_subject.route("/findById/<string:id_subject>", methods=["GET"])
def get_subject_by_id(id_subject):
    return SubjectService.get_subject_by_id(id_subject)


@bp_subject.route("/findAll", methods=["GET"])
def get_all_subjects():
    return SubjectService.get_all_subjects()


@bp_subject.route("/findByName/<string:name>", methods=["GET"])
def get_subject_by_name(name):
    return SubjectService.get_subject_by_name(name)


@bp_subject.route("/update/<string:id_subject>", methods=["PUT"])
def update_subject(id_subject):
    return SubjectService.update_subject(id_subject, request)


@bp_subject.route("/delete/<string:id_subject>", methods=["DELETE"])
def delete_subject(id_subject):
    return SubjectService.delete_subject(id_subject)
