from db import database
from models.client import professor


class Classroom(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    number = database.Column(database.Integer, nullable=False)
    id_professor = database.Column(database.Integer, database.ForeignKey(professor.Professor.id), nullable=False)
