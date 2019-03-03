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
	id = str(uuid.uuid4())
	return id

@app.route("/user/<id>")
def connect(id):
	coll = mongo.db[id]
	return render_template("index.html", id=id)

@app.route("/upload/<id>", methods=["POST"])
def upload(id):
	coll = mongo.db[id]
	app.logger.info("HELLO")
	f = request.files['file']
	if f:
		print(f, file=sys.stderr)
	else:
		print("Error", file=sys.stderr)
	#mongo.save_file(id, f)
	coll.insert({'name':f.filename, 'data':f.read()})
	print("uploaded")
	return redirect(url_for('connect', id=id))

@app.route("/retrieve/<id>")
def getUpload(id):
	coll = mongo.db[id]
	f= coll.find();
	total="";
	for imgs in f:
		return imgs["data"]
	#f= mongo.send_file(id)
	#return total

@app.route("/delete/<id>")
def delete(id):
	coll = mongo.db[id]
	numDeleted  = coll.delete_many({})
	return "deleted " + str(numDeleted.deleted_count)

if __name__ == "__main__":
	app.run(debug=True)
