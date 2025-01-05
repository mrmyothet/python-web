from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import User, db


login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:admin123!@localhost/Blog"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)  # Bind the db instance to this app
    login_manager.init_app(app)

    # Set the login view (for redirecting unauthorized users)
    login_manager.login_view = "user_routes.login"  # 'login' route from user_routes

    # Define user_loader function
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load the user by ID

    # Import and register blueprints
    from .routes.tweet import tweet_routes
    from .routes.user import user_routes
    from .routes.comment import comment_routes

    app.register_blueprint(tweet_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(comment_routes)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
