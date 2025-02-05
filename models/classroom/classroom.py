import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.professor import professor


class Classroom(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    number = database.Column(database.Integer, nullable=False)
    year = database.Column(database.Integer, nullable=False)
    status = database.Column(database.String(20), nullable=False)
    id_professor = database.Column(UUID(as_uuid=True), database.ForeignKey(professor.Professor.id), nullable=False)

    def __init__(self, number, year, status, id_professor):
        self.number = number
        self.year = year
        self.status = status
        self.id_professor = id_professor

    def to_dict(self):
        return {"id": self.id,
                "number": self.number,
                "year": self.year,
                "status": self.status,
                "id_professor": self.id_professor}
