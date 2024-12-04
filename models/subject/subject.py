from ...db import database


class Subject(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(120), nullable=False)
