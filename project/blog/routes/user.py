from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User, db

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the email is already registered
        if User.query.filter_by(email=email).first():
            flash("Email already registered!", "danger")
            return redirect(url_for("user_routes.register"))

        # Hash the password and create the new user
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("user_routes.login"))

    return render_template("register.html")


@user_routes.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if the user exists
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Invalid email or password!", "danger")
            return redirect(url_for("user_routes.login"))

        # Log the user in
        login_user(
            user
        )  # This sets the session and makes the user available via `current_user`
        flash("Login successful!", "success")
        return redirect(url_for("tweet_routes.list_tweets"))

    return render_template("login.html")


@user_routes.route("/logout")
@login_required  # Ensure the user is logged in before they can log out
def logout():
    logout_user()  # This clears the session and logs the user out
    flash("Logged out successfully!", "success")
    return redirect(url_for("user_routes.login"))


@user_routes.route("/users")
@login_required  # Protect this route so only logged-in users can access it
def list_users():
    users = User.query.all()
    return render_template("users.html", users=users)
