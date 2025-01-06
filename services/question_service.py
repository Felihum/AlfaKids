from flask import Request, jsonify
from db import database
from models.question.question import Question
from models.question.objective_question import ObjectiveQuestion
from models.question.discursive_question import DiscursiveQuestion
from models.question.question_type import QuestionType


class QuestionService:
    @staticmethod
    def create_question(request: Request):
        request_question = request.get_json()

        statement: str = request_question["statement"]
        question_type: str = request_question["type"]
        id_activity: int = request_question["id_activity"]

        if question_type.upper() == QuestionType.DISCURSIVE.name:
            expected_answer: str = request_question["expected_answer"]

            if not statement or not question_type or not id_activity or not expected_answer:
                return jsonify({"error": "Some field(s) has no value."}), 400

            question: Question = Question(statement, question_type, id_activity)
            new_discursive_question: DiscursiveQuestion = DiscursiveQuestion(question.statement, question.type,
                                                                             question.id_activity, question.id,
                                                                             expected_answer)

            database.session.add(new_discursive_question)
            database.session.commit()

            return jsonify({"message": "Question registered successfully!",
                            "question": new_discursive_question.to_dict()}), 201

        elif question_type.upper() == QuestionType.OBJECTIVE.name:

            answer1: str = request_question["answer1"]
            answer2: str = request_question["answer2"]
            answer3: str = request_question["answer3"]
            answer4: str = request_question["answer4"]
            right_answer: str = request_question["right_answer"]

            if (not statement or not question_type
                    or not id_activity or not answer1
                    or not answer2 or not answer3
                    or not answer4 or not right_answer):
                return jsonify({"error": "Some field(s) has no value."}), 400

            question: Question = Question(statement, question_type, id_activity)
            new_objective_question: ObjectiveQuestion = ObjectiveQuestion(question.statement, question.type,
                                                                          question.id_activity, question.id,
                                                                          answer1, answer2,
                                                                          answer3, answer4,
                                                                          right_answer)
            database.session.add(new_objective_question)
            database.session.commit()

            return jsonify({"message": "Question registered successfully!",
                            "question": new_objective_question.to_dict()}), 201

    @staticmethod
    def get_question_by_id(id_question: int):
        objective_question = ObjectiveQuestion.query.get(id_question)
        if objective_question:
            return jsonify({"message": "Question found",
                            "question": objective_question.to_dict()}), 200

        discursive_question = DiscursiveQuestion.query.get(id_question)
        if discursive_question:
            return jsonify({"message": "Question found",
                            "question": discursive_question.to_dict()}), 200

        return jsonify({"error": "Question not found!"}), 404

    @staticmethod
    def get_questions_by_activity_id(id_activity: int):
        objective_questions = ObjectiveQuestion.query.filter_by(id_activity=id_activity).all()
        discursive_questions = DiscursiveQuestion.query.filter_by(id_activity=id_activity).all()

        question_dict_list = []

        #question_dict_list.append([objective_question.to_dict() for objective_question in objective_questions])
        #question_dict_list.append([discursive_question.to_dict() for discursive_question in discursive_questions])

        for question in objective_questions:
            question_dict_list.append(question.to_dict())

        for question in discursive_questions:
            question_dict_list.append(question.to_dict())

        return jsonify({"message": "Question found",
                        "questions": question_dict_list}), 200

    @staticmethod
    def update_question(id_question: int, request: Request):
        request_question = request.get_json()

        statement: str = request_question["statement"]

        discursive_question: DiscursiveQuestion = DiscursiveQuestion.query.get(id_question)
        if discursive_question:
            expected_answer: str = request_question["expected_answer"]

            if not statement or not expected_answer:
                return jsonify({"error": "Some field(s) has no value."}), 400

            discursive_question.statement = statement
            discursive_question.expected_answer = expected_answer

            database.session.commit()

            return jsonify({"message": "Question updated successfully!",
                            "question": discursive_question.to_dict()}), 201

        objective_question: ObjectiveQuestion = ObjectiveQuestion.query.get(id_question)
        if objective_question:
            answer1: str = request_question["answer1"]
            answer2: str = request_question["answer2"]
            answer3: str = request_question["answer3"]
            answer4: str = request_question["answer4"]
            right_answer: str = request_question["right_answer"]

            if not statement or not answer1 or not answer2 or not answer3 or not answer4 or not right_answer:
                return jsonify({"error": "Some field(s) has no value."}), 400

            objective_question.statement = statement
            objective_question.answer1 = answer1
            objective_question.answer2 = answer2
            objective_question.answer3 = answer3
            objective_question.answer4 = answer4
            objective_question.right_answer = right_answer

            database.session.commit()

            return jsonify({"message": "Question updated successfully!",
                            "question": objective_question.to_dict()}), 201

    @staticmethod
    def delete_question(id_question):
        question: Question = Question.query.get(id_question)

        if not question:
            return jsonify({"error": "Question not found"}), 404

        objective_question = ObjectiveQuestion.query.filter_by(id_question=question.id).first()
        if objective_question:
            database.session.delete(objective_question)
            database.session.delete(question)
            database.session.commit()
            return jsonify({"message": "Question deleted successfully!"}), 200

        discursive_question = DiscursiveQuestion.query.filter_by(id_question=question.id).first()
        if discursive_question:
            database.session.delete(discursive_question)
            database.session.delete(question)
            database.session.commit()
            return jsonify({"message": "Question deleted successfully!"}), 200

        database.session.delete(question)
        database.session.commit()

        return jsonify({"message": "Question deleted successfully!"}), 200
