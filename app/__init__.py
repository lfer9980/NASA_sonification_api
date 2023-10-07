from flask import Flask
from flask_cors import CORS

def create_app():
    
    app = Flask(__name__)

    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from .public import public_bp
    app.register_blueprint(public_bp)
    
    return app