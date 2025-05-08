import uuid
from src.db import database
from sqlalchemy.dialects.postgresql import UUID


class Subject(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = database.Column(database.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"id": str(self.id),
                "name": self.name}
