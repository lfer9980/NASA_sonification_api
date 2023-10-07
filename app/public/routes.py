import time
from flask import Flask,jsonify,request
from . import public_bp

app = Flask(__name__)

@public_bp.route('/')
def index():
   message = {'content': 'API RESTful',
               'body': '',
               'images': '',}
   return message

@public_bp.route('/api/v1/time', methods= ['GET'])
def get_time():
    if(request.method == 'GET'): 
        return jsonify({'data': time.time()})