#app/main.py

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home_view():
        return "<h1>Hello World!</h1>"