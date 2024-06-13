from core import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    users_from_group = db.relationship("Group", backref = db.backref("users_from_group"))

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable=False)

class Timetable(db.Model):
    __tablename__ = "timetable"
    id = db.Column(db.Integer, primary_key = True)
    group = db.Column(db.Integer, db.ForeignKey("groups.id"))
    day = db.Column(db.String, nullable = True)
    time = db.Column(db.String, nullable = True)
    group_info = db.relationship("Group", backref=db.backref("timetable"))

class Dictionary(db.Model):
    __tablename__ = "dictionary"
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String, unique = True, nullable = False)
    rus = db.Column(db.String, nullable = False)
    eng = db.Column(db.String, nullable = False)
    deu = db.Column(db.String, nullable = False)
    word = db.Column(db.String, unique = True, nullable = False)

class Chat(db.Model):
    __tablename__ = "chats"
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    text = db.Column(db.String, nullable = False)
    time = db.Column(db.String, nullable = False)
    user_info = db.relationship("User", backref = db.backref("chats"))

class workbase(db.Model):
    __tablename__ = "workbase"
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String, nullable = False) # <- ???
    time = db.Column(db.String, nullable = False)