from ...db import database


class Client(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80), nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(120), nullable=False)
    age = database.Column(database.Integer, nullable=False)
    gender = database.Column(database.String(120), nullable=False)
