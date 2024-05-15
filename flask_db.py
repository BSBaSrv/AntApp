from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer,(80), unique = True, nullable=False)

class Group(db.Model):
    id = db.Integer(db.Integer, primary_key = True)
    name = db.String(db.String, unique = True, nullable=False)

class Timetable(db.Model):
    id = db.Integer(db.Integer, primary_key = True)
    group = db.String(db.String, unique = True, nullable = True)
    day = db.String(db.String, unique = True, nullable = True)
    time = db.String(db.String, unique = True, nullable = True)

class Dictionary(db.Model):
    id = db.Integer(db.Integer, primary_key = True)
    subject = db.String(db.String, unique = True, nullable = False)
    language = db.String(db.String, unique = True, nullable = False)
    word = db.String(db.String, unique = True, nullable = False)

class Chat(db.Model):
    message_id = db.Integer(db.Integer, primary_key = True)
    user = db.Integer(db.Integer, unique = True, nullable = False)
    text = db.String(db.String, unique = True, nullable = False)
    time = db.String(db.String, unique = True, nullable = False)

#Приколы и проблемы: нужно как-то связать: id(user) и user(chat), id(group) и group(timetable), group_id(user) и id(group).
#Также, я не уверен в том, что нужно писать db.TypeOfVariable, а не db.Column (как в class User). Ну это короче Константин придумал, так что все вопросы к нему.
#Если проблема решена - удалите комментарий о ней.
