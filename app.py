from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def create_app():
    # Create the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Import routes and models here to avoid circular imports
    from app import routes, models

    # Ensure database tables are created
    with app.app_context():
        db.create_all()

    # Register blueprints from routes
    app.register_blueprint(routes.bp)

    return app

# Create the app instance
app = create_app()

# Entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)
