from models.subject import subject
from db import database


class Professor(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)
    age = database.Column(database.Integer, nullable=False)
    gender = database.Column(database.String(120), nullable=False)
    id_subject = database.Column(database.Integer, database.ForeignKey(subject.Subject.id), nullable=False)
