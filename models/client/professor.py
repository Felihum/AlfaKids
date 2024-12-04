import client
from models.subject import subject
from db import database


class Professor(client.Client, database.Model):
    id_subject = database.Column(database.Integer, database.ForeignKey(subject.Subject.id), nullable=False)
