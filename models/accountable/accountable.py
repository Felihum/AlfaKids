from db import database
from models.client import client


class Accountable(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    name = database.Column(database.String(80), nullable=False)
    id_student = database.Column(database.Integer, database.ForeignKey(client.Client.id), nullable=False)
