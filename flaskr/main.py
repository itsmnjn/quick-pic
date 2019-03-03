from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import sys
import uuid
import dns

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'insta-doc-pic'
app.config["MONGO_URI"] = "mongodb+srv://Admin:Password@insta-doc-pic-czey7.gcp.mongodb.net/test?retryWrites=true"
#app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024
mongo = PyMongo(app)
#client = MongoClient('localhost', 27017)

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
	mongo.save_file(id, f)
	print( "uploaded")
	return redirect(url_for('connect', id=id))

@app.route("/retrieve/<id>")
def getUpload(id):
	return mongo.send_file(id)

if __name__ == "__main__":
	app.run(debug=True)
