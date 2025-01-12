from db import database
from models.student import student
from models.activity import activity


class StudentAccomplishment(database.Model):
    id_activity = database.Column(database.Integer, database.ForeignKey(activity.Activity.id), primary_key=True)
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), primary_key=True)

    def __init__(self, id_activity, id_student):
        self.id_activity = id_activity
        self.id_student = id_student

    def to_dict(self):
        return {"id_activity": self.id_activity,
                "id_student": self.id_student}
