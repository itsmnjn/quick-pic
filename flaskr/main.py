from flask import Flask,render_template
from flask_pymongo import PyMongo
import uuid
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def returnUniqueString():
	#GENERATE UNIQUE ID
	return str(uuid.uuid4())

@app.route("/user/<id>")
def connect(id):
	return render_template("index.html")

@app.route("/upload/<id>")
def upload(id):
	file = request.files["inputImages"]
	mongo.save_file(id+"1",

if __name__ == "__main__":
	app.run(debug=True)
