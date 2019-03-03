from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
import sys
import uuid
import dns
import mimetypes

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'insta-doc-pic'
app.config["MONGO_URI"] = "mongodb://Admin:Password@insta-doc-pic-shard-00-00-czey7.gcp.mongodb.net:27017,insta-doc-pic-shard-00-01-czey7.gcp.mongodb.net:27017,insta-doc-pic-shard-00-02-czey7.gcp.mongodb.net:27017/test?ssl=true&replicaSet=insta-doc-pic-shard-0&authSource=admin&retryWrites=true"

mongo = PyMongo(app)
db = mongo.cx['ids']

@app.route("/")
def returnUniqueString():
    #GENERATE UNIQUE ID
    id = str(uuid.uuid4())
    resp = make_response(id)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/user/<id>")
def connect(id):
    resp = make_response(render_template("index.html", id=id))
    return resp

@app.route("/upload/<id>", methods=["POST"])
def upload(id):
    coll = db[id]
    app.logger.info("HELLO")

    response = request.files['file']
    image = response.read()

    coll.insert_one({ 'name': response.filename, 'data': image })
    return redirect(url_for('connect', id=id))

@app.route("/retrieve/<id>")
def getUpload(id):
    coll = db[id]
    f = coll.find_one_and_delete({})

    if not f:
        return ""
    
    contentType = mimetypes.guess_type(f["name"])

    if not contentType[0]:
        contentType[0] = "image/jpeg"
    
    resp = make_response(f["data"])
    resp.headers["Content-Type"] = contentType[0]
    
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=8080)
