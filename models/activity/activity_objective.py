from db import database
from models.client import professor


class ActivityObjective(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.Text(), nullable=False)
    id_professor = database.Column(database.Integer, database.ForeignKey(professor.Professor.id), nullable=False)
    answer1 = database.Column(database.String(120), nullable=False)
    answer2 = database.Column(database.String(120), nullable=False)
    answer3 = database.Column(database.String(120), nullable=False)
    answer4 = database.Column(database.String(120), nullable=False)
    right_answer = database.Column(database.String(120), nullable=False)
