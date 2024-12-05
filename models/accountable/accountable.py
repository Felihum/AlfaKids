from db import database
from models.client import student


class Accountable(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), nullable=False)
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), nullable=False)
