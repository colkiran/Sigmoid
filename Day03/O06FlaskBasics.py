
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2> Hello World </h2>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h2> Greetings {usrname}, Welcome to the event..."

if __name__ == '__main__':
    app.run(debug=True)
