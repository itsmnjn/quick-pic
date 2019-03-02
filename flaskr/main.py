from flask import Flask,render_template, request
from flask_pymongo import PyMongo
import uuid
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
mongo = PyMongo(app)

@app.route("/")
def returnUniqueString():
	#GENERATE UNIQUE ID
	return str(uuid.uuid4())

@app.route("/user/<id>")
def connect(id):
	return render_template("index.html")

@app.route("/upload/<id>",methods=["POST"])
def upload(id):
	file = request.files["file"]
	mongo.save_file(id+str(uuid.uuid4()),file)
	return "uploaded"
	

if __name__ == "__main__":
	app.run(debug=True)
