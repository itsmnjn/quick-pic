from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def fun():
    fun()

def fun2():
    fun2()

def fun3():
    fun3()
