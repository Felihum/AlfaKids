from db import database
from models.subject import subject
from models.student import student


class Activity(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    title = database.Column(database.Text(), nullable=False)
    status = database.Column(database.String(20), nullable=False)
    id_subject = database.Column(database.Integer, database.ForeignKey(subject.Subject.id), nullable=False)
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), nullable=False)

    def __init__(self, title, status, id_subject, id_student):
        self.title = title
        self.status = status
        self.id_subject = id_subject
        self.id_student = id_student

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "status": self.status,
                "id_subject": self.id_subject,
                "id_student": self.id_student}
