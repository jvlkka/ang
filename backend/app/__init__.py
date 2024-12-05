"""
Main application factory module for the Flask backend.
This module initializes and configures the Flask application with all necessary extensions.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize extensions outside of create_app to avoid circular imports
db = SQLAlchemy()  # Database instance
jwt = JWTManager()  # JWT manager for handling authentication tokens

def create_app():
    """
    Application factory function that creates and configures the Flask app.
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Configure Flask app with necessary settings
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')  # Used for session management
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///voicebot.db')  # Database connection string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy event system (improves performance)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'jwt-secret-change-in-production')  # Secret for JWT encoding
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # Token expiration time

    # Initialize extensions with our application
    CORS(app)  # Enable Cross-Origin Resource Sharing
    db.init_app(app)  # Initialize database with app context
    jwt.init_app(app)  # Initialize JWT manager

    # Import and register blueprints (routes)
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Create all database tables within app context
    with app.app_context():
        db.create_all()

    return app
