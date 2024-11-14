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

    # Import and register the blueprint AFTER initializing the app and db
    from app.routes import bp as routes_bp  # Correctly reference the routes in the 'app' folder
    app.register_blueprint(routes_bp)

    # Ensure database tables are created within the app context
    with app.app_context():
        from app import models  # Correctly reference models in the 'app' folder
        db.create_all()

    return app

# Create the app instance
app = create_app()

# Entry point for running the app
if __name__ == "__main__":
    app.run(debug=True)
