from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import render_template
from waitress import serve
from flask_cors import CORS

import sys
sys.path.insert(0, './app/')

from index import index_app
from login import login_app
from mainpage import mainpage_app
from register import register_app
from edit_user import edit_user_app

#Se modifica para el despliegue
app = Flask(__name__,
            static_folder='../cliente/dist/static',
            template_folder='../cliente/dist')
app.config.from_object(__name__)
cors = CORS(app, resources= { r"/api/*": {"origins": "*"} } )
app.register_blueprint(index_app)
app.register_blueprint(login_app)
app.register_blueprint(mainpage_app)
app.register_blueprint(register_app)
app.register_blueprint(edit_user_app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

#app.run(host='0.0.0.0', debug= True)
serve(app, host='0.0.0.0', port=5000)
