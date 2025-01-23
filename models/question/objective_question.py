import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.question import question


class ObjectiveQuestion(question.Question, database.Model):
    id_question = database.Column(UUID(as_uuid=True), database.ForeignKey(question.Question.id), primary_key=True, unique=True, nullable=False)
    answer1 = database.Column(database.String(120), nullable=False)
    answer2 = database.Column(database.String(120), nullable=False)
    answer3 = database.Column(database.String(120), nullable=False)
    answer4 = database.Column(database.String(120), nullable=False)
    right_answer = database.Column(database.String(120), nullable=False)

    def __init__(self, statement, question_type, id_activity, id_question, answer1, answer2, answer3, answer4, right_answer):
        super().__init__(statement, question_type, id_activity)
        self.id_question = id_question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.right_answer = right_answer

    def to_dict(self):
        question_dict = super().to_dict()

        return {**question_dict,
                "answer1": self.answer1,
                "answer2": self.answer2,
                "answer3": self.answer3,
                "answer4": self.answer4,
                "right_answer": self.right_answer}

