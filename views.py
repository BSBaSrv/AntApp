from flask import jsonify, request
import base64
from core import app
from models import *


#ЧК Пользователя
@app.route("/user", methods = ["POST", "GET"])
def user():
  if request.method == "POST":
    user_id = request.form.get()

  if request.method == "GET":
    return jsonify(db.session.query(User).get(user_id))

@app.route("/register", methods = ["POST", "GET"])
def register():
  if request.method == "POST":
      reg_username = request.form.get()
      reg_password = request.form.get()
      reg_group_id = request.form.get() 

      for num in range(db.session.query(User).order_by(User.id)[-1]):
        if num["username"] == reg_username:
          status = False
        else:
          db.session.add(User(username = reg_username, password = reg_password, group_id = reg_group_id))
          db.session.commit()
          status = db.session.query(User).get(User(username = reg_username, password = reg_password, group_id = reg_group_id).id)

  #Если status == False, тo это значит, что пользователь с таким именем уже существует.
  #Если status == (то, что ввёл пользователь), то это значит, что регистрация прошла успешно (если мы конечно ещё где-то не облажались).
  if request.method == "GET":
    return jsonify(status)

@app.route("/login", methods = ["POST", "GET"])
def login():
  if request.method == "POST":
      log_username = request.form.get()
      log_password = request.form.get()

      for num in range(db.session.query(User).order_by(User.id)[-1]):
        if num["username"] == log_username:
          if db.session.query(User.password).filter_by(username = log_username).one() == log_password:
            status = db.session.query(User).filter_by(username = log_username).one()
          else:
            status = False
        else:
          status = False

  #Если status == False, то имя или пароль неправильные.
  #Если status == (данные из БД), то такие данные есть и пользователю можно дать право использовать эти данные.
  if request.method == "GET":
    return jsonify(status)

#ЧК Группы
@app.route("/group", methods = ["POST", "GET"])
def group():
  if request.method == "POST":
    group_id = request.form.get("")

  if request.method == "GET":
    return jsonify(db.session.query(Group).get(group_id))

@app.route("/timetable", methods = ["POST", "GET"])
def timetable():
  if request.method == "POST":
    timetable_id = request.form.get()

  if request.method == "GET":
    return jsonify(db.session.query(Timetable).get(timetable_id))

#ЧК Социальных инструментов
@app.route("/chat", methods = ["POST", "GET"])
def chat():
  if request.method == "POST":
    mes_user = request.form.get()
    mes_text = request.form.get()
    mes_time = request.form.get()

    db.session.add(Chat(user = mes_user, text = mes_text, time = mes_time))
    db.session.commit()

  if request.method == "GET":
    return jsonify(db.session.query(Chat).all()) #Поменяйте потом на вывод последних (например) 100 сообщений, ибо я просто хз, как выводить строчки - в виде словаря списка или что там ещё.

@app.route("/workbase", methods = ["POST", "GET"])
def workbase():
  if request.method == "POST":
    image_bytecode = request.form.get() #Я хз, как будут выглядить картинки, но предполагаю, что это будет base64-код.
    image_time = request.form.get()

    db.session.add(Workbase(image = image_bytecode, time = image_time))
    db.session.commit()

  if request.method == "GET":
    return jsonify(db.session.query(Workbase).all()) #Аналогично с 85 строкой.

#ЧК Словаря
@app.route("/dictionary")
def get_dict():
  return jsonify(db.session.query(Dictionary).all())