from flask import Blueprint, request
from services.professor_service import ProfessorService

bp_professor = Blueprint("professor", __name__, url_prefix="/professor")


@bp_professor.route("/register", methods=["POST"])
def create_professor():
    return ProfessorService.create_professor(request)


@bp_professor.route("/findById/<int:id_professor>", methods=["GET"])
def get_professor_by_id(id_professor):
    return ProfessorService.get_professor_by_id(id_professor)


@bp_professor.route("/findByEmail/<string:email>", methods=["GET"])
def get_professor_by_email(email):
    return ProfessorService.get_professor_by_email(email)


@bp_professor.route("/update/<int:id_professor>", methods=["PUT"])
def update_professor(id_professor):
    return ProfessorService.update_professor(id_professor, request)


@bp_professor.route("/delete/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    return ProfessorService.delete_professor(id_professor)
