import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID
from models.classroom import classroom
from models.activity import activity


class ActivityDistribution(database.Model):
    id_activity = database.Column(UUID(as_uuid=True), database.ForeignKey(activity.Activity.id), primary_key=True)
    id_classroom = database.Column(UUID(as_uuid=True), database.ForeignKey(classroom.Classroom.id), primary_key=True)

    def __init__(self, id_activity, id_classroom):
        self.id_activity = id_activity
        self.id_classroom = id_classroom

    def to_dict(self):
        return {"id_activity": self.id_activity,
                "id_classroom": self.id_classroom}
