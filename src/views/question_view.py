from flask import Blueprint, request
from src.services.question_service import QuestionService

bp_question = Blueprint("question", __name__, url_prefix="/question")


@bp_question.route("/register", methods=["POST"])
def create_question():
    return QuestionService.create_question(request)


@bp_question.route("/findById/<string:id_question>", methods=["GET"])
def get_question_by_id(id_question):
    return QuestionService.get_question_by_id(id_question)


@bp_question.route("/findByActivityId/<string:id_activity>", methods=["GET"])
def get_question_by_activity_id(id_activity):
    return QuestionService.get_questions_by_activity_id(id_activity)


@bp_question.route("/update/<string:id_question>", methods=["PUT"])
def update_question(id_question):
    return QuestionService.update_question(id_question, request)


@bp_question.route("/delete/<string:id_question>", methods=["DELETE"])
def delete_question(id_question):
    return QuestionService.delete_question(id_question)
