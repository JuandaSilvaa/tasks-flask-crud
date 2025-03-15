from flask import Flask

# __name__ = '__main__ quando roda de forma manual
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello world!"

@app.route("/about")
def about():
  return "Página sobre"

# debug=True habilita os logs
# isso e so para desenvolvimento local, quando rodamos de forma manual
if __name__ == "__main__":
  app.run(debug=True)