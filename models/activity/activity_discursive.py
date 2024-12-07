from db import database
from models.subject import subject


class ActivityDiscursive(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.Text(), nullable=False)
    id_subject = database.Column(database.Integer, database.ForeignKey(subject.Subject.id), nullable=False)
    answer = database.Column(database.Text(), nullable=False)
    expected_answer = database.Column(database.Text(), nullable=False)
