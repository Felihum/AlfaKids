from src.models.student import student
from src.models.activity import activity
from src.db import database
from sqlalchemy.dialects.postgresql import UUID


class StudentAccomplishment(database.Model):
    id_activity = database.Column(UUID(as_uuid=True), database.ForeignKey(activity.Activity.id), primary_key=True, nullable=False)
    id_student = database.Column(UUID(as_uuid=True), database.ForeignKey(student.Student.id), primary_key=True, nullable=False)

    def __init__(self, id_activity, id_student):
        self.id_activity = id_activity
        self.id_student = id_student

    def to_dict(self):
        return {"id_activity": self.id_activity,
                "id_student": self.id_student}
