from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app import routes, models

# Initialize the SQLAlchemy object globally
db = SQLAlchemy()

def create_app():
    # Create Flask app instance
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object(Config)
    
    # Initialize the database with the app
    db.init_app(app)

    # Register blueprints and create database tables
    with app.app_context():
        db.create_all()  # Ensure database tables are created

    # Register routes blueprint
    app.register_blueprint(routes.bp)

    return app

# Create the app instance
app = create_app()

# If this script is run directly, start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
