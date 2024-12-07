from db import database
from models.question import question


class DiscursiveQuestion(question.Question, database.Model):
    id_question = database.Column(database.Integer, database.ForeignKey(question.Question.id), primary_key=True, nullable=False)
    answer = database.Column(database.Text(), nullable=False)
    expected_answer = database.Column(database.Text(), nullable=False)