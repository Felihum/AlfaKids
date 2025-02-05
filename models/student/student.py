import uuid
from db import database
from sqlalchemy.dialects.postgresql import UUID


class Student(database.Model):
    id = database.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)
    age = database.Column(database.Integer, nullable=False)
    gender = database.Column(database.String(120), nullable=False)
    autism_level = database.Column(database.Integer, nullable=False)
    school_year = database.Column(database.Integer, nullable=False)

    def __init__(self, name, email, password, age, gender, autism_level, school_year):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.autism_level = autism_level
        self.school_year = school_year

    def to_dict(self):
        return {"id": str(self.id),
                "name": self.name,
                "email": self.email,
                "password": self.password,
                "age": self.age,
                "gender": self.gender,
                "autism_level": self.autism_level,
                "school_year": self.school_year}
