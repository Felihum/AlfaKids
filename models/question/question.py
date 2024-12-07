from db import database
from models.activity import activity


class Question(database.Model):
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    statement = database.Column(database.Text(), nullable=False)
    type = database.Column(database.String(20), nullable=False)
    id_activity = database.Column(database.Integer, database.ForeignKey(activity.Activity.id), nullable=False)
