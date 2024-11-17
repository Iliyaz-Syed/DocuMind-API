"""
Main application package.
"""
from flask import Flask
from app.api.routes import api
from app.config.settings import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(api, url_prefix='/api')
    return app 