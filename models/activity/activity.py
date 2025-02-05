import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.subject import subject
from models.professor import professor


class Activity(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = database.Column(database.Text(), nullable=False)
    status = database.Column(database.String(20), nullable=False)
    id_subject = database.Column(UUID(as_uuid=True), database.ForeignKey(subject.Subject.id), nullable=False)
    id_professor = database.Column(UUID(as_uuid=True), database.ForeignKey(professor.Professor.id), nullable=False)

    def __init__(self, title, status, id_subject, id_professor):
        self.title = title
        self.status = status
        self.id_subject = id_subject
        self.id_professor = id_professor

    def to_dict(self):
        return {"id": self.id,
                "title": self.title,
                "status": self.status,
                "id_subject": self.id_subject,
                "id_professor": self.id_professor}
