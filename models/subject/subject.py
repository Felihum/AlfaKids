from db import database


class Subject(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(120), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"id": self.id,
                "name": self.name}
