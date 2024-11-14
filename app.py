# app.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    """Factory function to initialize and configure the app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)

    # Import and register blueprints to avoid circular imports
    with app.app_context():
        from app import routes, models  # Import routes and models here to avoid circular dependencies
        db.create_all()  # Ensure database tables are created
        app.register_blueprint(routes.bp)  # Register the blueprint for routes

    return app

# Create an app instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
