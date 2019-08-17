from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from pymongo import MongoClient
import json
import sys

register_app = Blueprint("register_app", __name__, template_folder="templates")

@register_app.route('/api/v1.0/register', methods=['POST'])
def registro():

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
      collection.insert_one({ "_id": j['username'],"name": j['name'],"email":j['email'],"password":j['password'],"comments":[]})
      return jsonify(True)
    except:
      return jsonify(False)