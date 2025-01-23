import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.student import student


class Accountable(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    telephone = database.Column(database.String(120), unique=True, nullable=False)
    id_student = database.Column(UUID(as_uuid=True), database.ForeignKey(student.Student.id), nullable=False)

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
