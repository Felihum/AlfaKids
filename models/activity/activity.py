from db import database
from models.subject import subject
from models.student import student


class Activity(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.Text(), nullable=False)
    id_subject = database.Column(database.Integer, database.ForeignKey(subject.Subject.id), nullable=False)
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), nullable=False)