from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:postgres@localhost:5434/Todo"
    )
    db.init_app(app)

    from .routes import bp

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app
