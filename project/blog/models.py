from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(50), nullable=True)
    birth_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    tweets = db.relationship(
        "Tweet", backref="author", lazy=True, cascade="all, delete-orphan"
    )
    comments = db.relationship(
        "Comment", backref="author", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        """Representation of the User for debugging purposes."""
        return f"<User {self.username}>"

    def display_name(self):
        """Return a formatted name for display purposes."""
        return self.username.capitalize()


# Define the Tweet model
class Tweet(db.Model):
    __tablename__ = "tweets"  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    comments = db.relationship(
        "Comment", backref="tweet", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        """Representation of the Tweet for debugging purposes."""
        return f"<Tweet {self.content[:50]}>"

    def formatted_date(self):
        """Return the creation date in a readable format."""
        return self.created_at.strftime("%b %d, %Y")


# Define the Comment model
class Comment(db.Model):
    __tablename__ = "comments"  # Table name in the database
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    tweet_id = db.Column(
        db.Integer, db.ForeignKey("tweets.id", ondelete="CASCADE"), nullable=False
    )
    content = db.Column(db.String(280), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    def __repr__(self):
        """Representation of the Comment for debugging purposes."""
        return f"<Comment {self.content[:50]}>"

    def formatted_date(self):
        """Return the creation date in a readable format."""
        return self.created_at.strftime("%b %d, %Y")
