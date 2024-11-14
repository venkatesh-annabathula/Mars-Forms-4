from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app import routes, models
    with app.app_context():
        db.create_all()  # Ensure database tables are created

    app.register_blueprint(routes.bp)
    return app
