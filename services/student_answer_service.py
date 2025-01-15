from flask import Request, jsonify
from models.student_answer.student_answer import StudentAnswer
from db import database


class StudentAnswerService:

    @staticmethod
    def create_answer(request: Request):
        request_answer: StudentAnswer = request.get_json()

        answer: str = request_answer["answer"]
        id_activity: int = request_answer["id_activity"]
        id_question: int = request_answer["id_question"]
        id_student: int = request_answer["id_student"]

        if not id_activity or not id_question or not id_student:
            return jsonify({"error": "Some field(s) has no value."}), 400

        new_answer: StudentAnswer = StudentAnswer(answer, id_activity, id_question, id_student)

        database.session.add(new_answer)
        database.session.commit()

        return jsonify({"message": "Answer registered successfully!",
                        "answer": new_answer.to_dict()}), 201

    @staticmethod
    def get_answers_by_activity_and_student_id(id_activity, id_student):
        answers = StudentAnswer.query.filter_by(id_activity=id_activity, id_student=id_student).all()

        if not answers:
            return jsonify({"error": "No answers found."}), 404

        answers_dict_list = [answer.to_dict() for answer in answers]

        return jsonify({"message": "Answers found",
                        "answers": answers_dict_list}), 200

    @staticmethod
    def get_answers_by_student_id(id_student):
        answer = StudentAnswer.query.filter_by(id_student=id_student).first()

        if not answer:
            return jsonify({"error": "No answer found."}), 404

        return jsonify({"message": "Answer found",
                        "answer": answer}), 200

    @staticmethod
    def get_answers_by_activity_id(id_activity):
        answer = StudentAnswer.query.filter_by(id_activity=id_activity).first()

        if not answer:
            return jsonify({"error": "No answer found."}), 404

        return jsonify({"message": "Answer found",
                        "answer": answer}), 200

    @staticmethod
    def get_answer_by_question_and_student_id(id_question, id_student):
        answer = StudentAnswer.query.filter_by(id_question=id_question, id_student=id_student).first()

        if not answer:
            return jsonify({"error": "No answer found."}), 404

        return jsonify({"message": "Answer found",
                        "answer": answer.to_dict()}), 200

    @staticmethod
    def delete_answer(id_answer):
        answer: StudentAnswer = StudentAnswer.query.get(id_answer)

        if not answer:
            return jsonify({"error": "Answer not found"}), 404

        database.session.delete(answer)
        database.session.commit()

        return jsonify({"message": "Answer deleted successfully!"}), 200
