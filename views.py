from core import app

# Теперь балбесы ваша задача - сделать простую логику загрузки данных. Конкретно - создать разные страницы, с которых
# будут возвращаться разные данные в зависимости от параметров запроса
# Например, chat будет возвращать последние сто сообщений (потом реализуем деление чата на страницы)
# /timetable/номер_группы - возвращает расписание для группы
# И так далее

@app.route("/user")
def user():
  return "Страница пользователя"

@app.route("/group")
def group():
  return "Группы"

@app.route("/timetable")
def timetable():
  return "Расписание"

@app.route("/dictionary")
def dictionary():
  return "Словарь"

@app.route("/chat")
def chat():
  return "Чаты"

@app.route("/workbase")
def workbase():
  return "Контрольные работы"
