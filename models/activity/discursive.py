from db import database
import activity


class Objective(database.Model, activity.Activity):
    answer = database.Column(database.Text(), nullable=False)
    expected_answer = database.Column(database.Text(), nullable=False)
