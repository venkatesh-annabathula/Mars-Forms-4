from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Import routes and models only after db and app have been initialized
    from app.routes import bp as routes_bp

    with app.app_context():
        db.create_all()  # Ensure database tables are created

    app.register_blueprint(routes_bp)
    return app

# Entry point for running the app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
