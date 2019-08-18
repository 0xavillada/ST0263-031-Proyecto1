from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from pymongo import MongoClient
import json
import sys

mainpage_app = Blueprint("mainpage_app", __name__, template_folder="templates")

@mainpage_app.route('/api/v1.0/mainpage', methods=['POST'])
def mainpageInit():

    j = json.loads(request.data)
    """
    criterio
    """
    MONGO_URL = 'mongodb://mongo-server'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']

    if j['criterio'] == 'all':
        consulta = collection.find()
        try:
            comentarios = []
            for r in consulta:
                indexInUser = 0
                for x in r['comments']:
                    comentarios.append((r['_id'],x['theme'],x['text'],indexInUser))
                    indexInUser = indexInUser + 1
                #print comentarios
            return jsonify(comentarios)
        except:
            # ese usuario no existe
            return jsonify(False)
        return jsonify(False)
        
    else:
        #solo los del usuario en criterio
        consulta = collection.find({"_id":j['criterio']})
        try:
            comentarios = []
            for r in consulta:
                indexInUser = 0
                for x in r['comments']:
                    comentarios.append((r['_id'],x['theme'],x['text'],indexInUser))
                    indexInUser = indexInUser + 1
                #print comentarios
                return jsonify(comentarios)
        except:
            # ese usuario no existe
            return jsonify(False)
        return jsonify(False)


@mainpage_app.route('/api/v1.0/mainpage/addComment', methods=['POST'])
def mainpageAddComment():
    
    j = json.loads(request.data)
    print j
    """
    username
    theme
    text
    """
    MONGO_URL = 'mongodb://mongo-server'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']
    
    try:
        collection.update( { "_id":j['username'] },{ "$push": { "comments": {"theme":j['theme'],"text":j['text'] } } } )
        return jsonify(True)
    except:
        return jsonify(False)
    return jsonify(False)

@mainpage_app.route('/api/v1.0/mainpage/byTheme', methods=['POST'])
def mainpageByTheme():
    
    j = json.loads(request.data)
    """
    theme
    """
    MONGO_URL = 'mongodb://mongo-server'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']

    consulta = collection.find()
    try:
        comentarios = []
        for r in consulta:
            indexInUser = 0
            for x in r['comments']:
                if j['theme'] == x['theme']:
                    comentarios.append((r['_id'],x['theme'],x['text'],indexInUser))
                indexInUser = indexInUser + 1
        return jsonify(comentarios)
    except:
        # ese usuario no existe
        return jsonify(False)
    return jsonify(False)

@mainpage_app.route('/api/v1.0/mainpage/editComment', methods=['POST'])
def mainpageEditComment():
    j = json.loads(request.data)
    """
    username
    theme
    text
    indexInUser
    """
    MONGO_URL = 'mongodb://mongo-server'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']
    
    try:
        collection.update( { "_id":j['username'] },{ "$set": { "comments."+str(j['indexInUser']):{ "theme": j['theme'], "text":j['text'] } } } )
        return jsonify(True)
    except:
        return jsonify(False)
    return jsonify(False)


@mainpage_app.route('/api/v1.0/mainpage/deleteComment', methods=['POST'])
def mainpageDeleteComment():
    
    j = json.loads(request.data)
    """
    username
    theme
    text
    """
    print j
    MONGO_URL = 'mongodb://mongo-server'
    client = MongoClient(MONGO_URL)
    db = client['python-vueDB']
    collection = db['usuarios']
    
    try:
        collection.update( { "_id":j['username'] },{ "$pull": { "comments": {"theme":j['theme'],"text":j['text'] } } } )
        return jsonify(True)
    except:
        return jsonify(False)
    return jsonify(False)
