# app package
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Imports after db to prevent circular import errors
from app.api import api_bp
from app.service.mqtt_service import start_mqtt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    app.register_blueprint(api_bp)
    
    # Create database tables for our models
    with app.app_context():
        db.create_all()
        
    start_mqtt()
    
    return app