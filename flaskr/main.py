from flask import Flask,render_template
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

@app.route("/")
def returnUniqueString():
	#GENERATE UNIQUE ID
	return "adfjkladsjfkladsjfkldasjklfjsd"

@app.route("/user/<id>")
def connect(id):
	return render_template("index.html")

@app.route("/upload/<id>")
def upload(id):
	mongo.save_file
	file = request.files["inputImages"]

if __name__ == "__main__":
	app.run(debug=True)