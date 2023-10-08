import os
from flask import Flask,jsonify,request
from . import public_bp
from werkzeug.utils import secure_filename

app = Flask(__name__)


@public_bp.before_app_request
def create_public_bp():
    UPLOAD_FOLDER = 'app/uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@public_bp.route('/')
def index():
   message = {'content': 'API RESTful',
               'body': '',
               'images': '',}
   return message

""" @public_bp.route('/api/v1/time', methods= ['GET'])
def get_time():
    if(request.method == 'GET'): 
        return jsonify({'data': time.time()}) """
    

@public_bp.route('/api/v1/upload', methods= ['POST'])
def upload_time():
    if(request.method == 'POST'): 
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'message': 'File uploaded successfully'})