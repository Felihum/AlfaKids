import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID


class Professor(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)
    registration = database.Column(database.String(120), unique=True, nullable=False)

    def __init__(self, name, email, password, registration):
        self.name = name
        self.email = email
        self.password = password
        self.registration = registration

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "registration": self.registration}
