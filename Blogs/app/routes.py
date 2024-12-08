from flask import Flask, render_template, request, redirect, url_for, session
from app.models import create_user, get_all_posts
from app.models import validate_user_login
from werkzeug.security import generate_password_hash


# blueprint routes
# normal routes

from app import app

app.secret_key = "Testing123"


@app.route("/")
def index():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"], method="pbkdf2")
        print(password)

        create_user(username, password, email)

        return "Register Successful"

    if request.method == "GET":
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = validate_user_login(username, password)
        if user:
            # return "Login Successful"

            session["user_id"] = user[0]
            return redirect(url_for("index"))

        return "Invalid Information"

    return render_template("login.html")
