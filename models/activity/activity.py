from db import database
from models.client import professor


class Activity(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.Text(), nullable=False)
    id_professor = database.Column(database.Integer, database.ForeignKey(professor.Professor.id), nullable=False)
