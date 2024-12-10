from db import database
from models.student import student


class Accountable(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    telephone = database.Column(database.String(120), unique=True, nullable=False)
    id_student = database.Column(database.Integer, database.ForeignKey(student.Student.id), nullable=False)

    def __init__(self, name, email, telephone, id_student):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.id_student = id_student

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "telephone": self.telephone,
                "id_student": self.id_student}
