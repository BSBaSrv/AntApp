from flask import Flask
app = Flask(__name__)


@app.route("/user")
def user():
  return

@app.route("/group")
def group():
  return

@app.route("/timetable")
def timetable():
  return

@app.route("/dictionary")
def dictionary():
  return

@app.route("/chat")
def chat():
  return

@app.route("/workbase")
def workbase():
  return


if __name__ == '__main__':
  app.run()