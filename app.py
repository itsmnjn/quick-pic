from flask import Flask
import uuid
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def generateID():
    return str(uuid.uuid4())
