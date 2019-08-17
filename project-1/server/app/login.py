from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from pymongo import MongoClient
import json
import sys

login_app = Blueprint("login_app", __name__, template_folder="templates")

@login_app.route('/api/v1.0/login', methods=['POST'])
def login():

    j = json.loads(request.data)
    
    """
    username
    password
    """
    MONGO_URL = 'mongodb://localhost'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']

    consulta = collection.find({"_id":j['username']})
    try:
      for r in consulta:

        if r['_id'] == j['username'] and r['password'] == j['password']:
          return jsonify(True)
        else:
          return jsonify(False)
    except:
      return jsonify(False)
    return jsonify(False)