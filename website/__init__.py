# website/__init__.py

import os
from flask import Flask
from .views import views

def create_app():
    app = Flask(__name__)

    # Set secret key and configurations
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif', 'mp4', 'avi', 'mov'}

    # Register Blueprint
    app.register_blueprint(views, url_prefix='/')

    return app

