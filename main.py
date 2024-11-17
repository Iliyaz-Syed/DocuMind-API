from flask import Flask
from app.api.routes import api
from app.config.settings import Config
from app.utils.logger import setup_logger

logger = setup_logger(__name__)

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000) 