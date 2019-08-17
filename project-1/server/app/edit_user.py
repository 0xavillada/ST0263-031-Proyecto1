from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from pymongo import MongoClient
import json
import sys

edit_user_app = Blueprint("edit_user_app", __name__, template_folder="templates")

@edit_user_app.route('/api/v1.0/mainpage/editUser', methods=['POST'])
def mainpage():
    j = json.loads(request.data)

    print j
    """
    username
    """
    MONGO_URL = 'mongodb://localhost'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']

    consulta = collection.find({"_id":j['username']})
    try:
      for r in consulta:
        print r['name'],r['password'],r['email']
        return jsonify(r['name'],r['password'],r['email'])
    except:
      return jsonify(False)
    return jsonify(False)

@edit_user_app.route('/api/v1.0/mainpage/editUser/confirm', methods=['POST'])
def mainpageConfirm():
    j = json.loads(request.data)

    """
    name
    email
    username
    password
    """

    MONGO_URL = 'mongodb://localhost'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']

    try:
      collection.update({ "_id": j['username'] }, { "$set": {"name": j['name'],"email":j['email'],"password":j['password']} } )
      return jsonify(True)
    except:
      return jsonify(False)