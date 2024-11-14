from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Function to create the app
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # Import routes and register blueprints AFTER the app and db initialization
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # Ensure database tables are created
    with app.app_context():
        from app import models  # Import models here to avoid circular imports
        db.create_all()

    return app

# Create the app instance
app = create_app()

# Entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)
