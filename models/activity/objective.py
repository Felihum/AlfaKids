from db import database
import activity


class Objective(database.Model, activity.Activity):
    answer1 = database.Column(database.String(120), nullable=False)
    answer2 = database.Column(database.String(120), nullable=False)
    answer3 = database.Column(database.String(120), nullable=False)
    answer4 = database.Column(database.String(120), nullable=False)
    right_answer = database.Column(database.String(120), nullable=False)
