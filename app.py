# app.py
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance globally here
db = SQLAlchemy()

def create_app():
    """Factory function to initialize and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database with the app
    db.init_app(app)

    # Import and register blueprints
    with app.app_context():
        from app import routes, models  # Import within app context to avoid circular imports
        db.create_all()  # Ensure database tables are created
        app.register_blueprint(routes.bp)  # Register the blueprint from routes

    return app

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
