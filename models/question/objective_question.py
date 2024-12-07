from db import database
from models.question import question


class ObjectiveQuestion(question.Question, database.Model):
    id_question = database.Column(database.Integer, database.ForeignKey(question.Question.id), primary_key=True, nullable=False)
    answer1 = database.Column(database.String(120), nullable=False)
    answer2 = database.Column(database.String(120), nullable=False)
    answer3 = database.Column(database.String(120), nullable=False)
    answer4 = database.Column(database.String(120), nullable=False)
    right_answer = database.Column(database.String(120), nullable=False)
