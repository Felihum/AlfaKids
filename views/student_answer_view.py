from flask import Blueprint, request
from services.student_answer_service import StudentAnswerService

bp_answer = Blueprint("answer", __name__, url_prefix="/answer")


@bp_answer.route("/register", methods=["POST"])
def create_answer():
    return StudentAnswerService.create_answer(request)


@bp_answer.route("/findByActivityAndStudentId/<string:id_activity>/<string:id_student>", methods=["GET"])
def get_answers_by_activity_and_student_id(id_activity, id_student):
    return StudentAnswerService.get_answers_by_activity_and_student_id(id_activity, id_student)


@bp_answer.route("/findByQuestionAndStudentId/<string:id_question>/<string:id_student>", methods=["GET"])
def get_answer_by_question_and_student_id(id_question, id_student):
    return StudentAnswerService.get_answer_by_question_and_student_id(id_question, id_student)


@bp_answer.route("/delete/<string:id_answer>", methods=["DELETE"])
def delete_answer(id_answer):
    return StudentAnswerService.delete_answer(id_answer)
