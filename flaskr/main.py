from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import sys
import uuid

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
mongo = PyMongo(app)

@app.route("/")
def returnUniqueString():
	#GENERATE UNIQUE ID
	return '''localhost:5000/user/''' + str(uuid.uuid4())

@app.route("/user/<id>")
def connect(id):
	return render_template("index.html", id=id)

@app.route("/upload/<id>", methods=["POST"])
def upload(id):
	app.logger.info("HELLO")
	f = request.files['file']

	if f:
		print(f, file=sys.stderr)
	else:
		print("FUCK", file=sys.stderr)
	# mongo.save_file(id+str(uuid.uuid4()),file)
	# return "uploaded"
	return redirect(url_for('connect', id=id))


if __name__ == "__main__":
	app.run(debug=True)
