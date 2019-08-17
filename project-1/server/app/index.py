from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
import sys

index_app = Blueprint("index_app", __name__, template_folder="templates")