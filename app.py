from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def return1():
    return 1

def return2():
    return 2
