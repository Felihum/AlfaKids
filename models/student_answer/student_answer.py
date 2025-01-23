import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.activity import activity
from models.question import question
from models.student import student


class StudentAnswer(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    answer = database.Column(database.Text(), nullable=False)
    id_activity = database.Column(UUID(as_uuid=True), database.ForeignKey(activity.Activity.id), nullable=False)
    id_question = database.Column(UUID(as_uuid=True), database.ForeignKey(question.Question.id), nullable=False)
    id_student = database.Column(UUID(as_uuid=True), database.ForeignKey(student.Student.id), nullable=False)

    def __init__(self, answer, id_activity, id_question, id_student):
        self.answer = answer
        self.id_activity = id_activity
        self.id_question = id_question
        self.id_student = id_student

    def to_dict(self):
        return {"id": self.id,
                "answer": self.answer,
                "id_activity": self.id_activity,
                "id_question": self.id_question,
                "id_student": self.id_student}
