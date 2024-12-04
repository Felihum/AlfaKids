from db import database
import client


class Student(client.Client, database.Model):
    autism_level = database.Column(database.Integer, nullable=False)
    school_year = database.Column(database.Integer, nullable=False)
