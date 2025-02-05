import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.question import question


class DiscursiveQuestion(question.Question, database.Model):
    id_question = database.Column(UUID(as_uuid=True), database.ForeignKey(question.Question.id), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    expected_answer = database.Column(database.Text(), nullable=False)

    def __init__(self, statement, question_type, id_activity, id_question, expected_answer):
        super().__init__(statement, question_type, id_activity)
        self.id_question = id_question
        self.expected_answer = expected_answer

    def to_dict(self):
        question_dict = super().to_dict()

        return {**question_dict,
                "expected_answer": self.expected_answer}
