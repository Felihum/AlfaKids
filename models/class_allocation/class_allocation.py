from db import database
from models.classroom import classroom
from models.student import student


class ClassAllocation(database.Model):
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), primary_key=True)
    id_classroom = database.Column(database.Integer, database.ForeignKey(classroom.Classroom.id), primary_key=True)

    def __init__(self, id_student, id_classroom):
        self.id_student = id_student
        self.id_classroom = id_classroom

    def to_dict(self):
        return {"id_student": self.id_student,
                "id_classroom": self.id_classroom}
