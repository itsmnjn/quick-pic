from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_pymongo import PyMongo
import sys
import uuid
import dns
import mimetypes

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "insta-doc-pic"
app.config["MONGO_URI"] = "mongodb://Admin:Password@insta-doc-pic-shard-00-00-czey7.gcp.mongodb.net:27017,insta-doc-pic-shard-00-01-czey7.gcp.mongodb.net:27017,insta-doc-pic-shard-00-02-czey7.gcp.mongodb.net:27017/test?ssl=true&replicaSet=insta-doc-pic-shard-0&authSource=admin&retryWrites=true"

mongo = PyMongo(app)
db = mongo.cx["ids"]


"""
#Main path
#returns a unique id string that identifies users

"""
@app.route("/")
def genID():
    id = str(uuid.uuid4())
    resp = make_response(id)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


"""
#User upload
#Allows users to upload images. The form that submits on image 
#upload sends a POST request to /upload/<id>

"""
@app.route("/user/<id>")
def user(id):
    resp = make_response(render_template("index.html", id = id))
    return resp


"""
#Uploads image to database
#Uploads the image sent through the POST request to a mongodb
#collection with the users id as the collection name.

"""
@app.route("/upload/<id>", methods = ["POST"])
def upload(id):
    coll = db[id]

    responses = request.files.getlist("files")
    
    for r in responses:
        filename = r.filename
        image = r.read()
        coll.insert_one({ "name": r.filename, "data": image })

    return redirect(url_for("user", id = id))

"""
#Retrieves image from database
#Retrieves the uploaded the image sent to the mongo database keyed
#with the users id. Then deletes all the images it retrieves. 

"""
@app.route("/retrieve/<id>")
def retrieve(id):
    coll = db[id]
    f = coll.find_one_and_delete({}, sort = [( "_id", 1 )]) # -1 sorts in descending order

    if not f:
        return ""
    
    contentType = mimetypes.guess_type(f["name"])

    if not contentType[0]:
        contentType[0] = "image/jpeg"
    
    resp = make_response(f["data"])
    resp.headers["Content-Type"] = contentType[0]
    
    return resp

"""
#Drops the database
#Drops the user's collection
"""

@app.route("/done/<id>")
def done(id):
    coll = db[id]
    coll.drop()
    return ""

@app.route("/google52e661dd7d186531.html")
def file():
    return render_template("google52e661dd7d186531.html")

if __name__ == "__main__":
    app.run(debug = True, port = 8080)
