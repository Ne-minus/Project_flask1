from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"


    user_id = db.Column('user_id', db.Text, ForeignKey('answers.user_id'), primary_key=True)


    answer = db.relationship('Answers')


    name = db.Column('name', db.Text)
    age = db.Column('age', db.Integer)


class Answers(db.Model):

    __tablename__ = "answers"

    user_id = db.Column('user_id', db.Integer, primary_key=True)
    ask1 = db.Column('answer1', db.Text)
    ask2 = db.Column('answer2', db.Text)

class Questions(db.Model):

    __tablename__ = "questions"

    question_id = db.Column('quest_id', db.Integer, primary_key=True)
    question_name = db.Column('quest_itself', db.Text)