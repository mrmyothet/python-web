from flask import Flask, render_template, request, redirect, url_for, session
from app.models import create_user, get_all_posts, get_user, add_post
from app.models import validate_user_login
from werkzeug.security import generate_password_hash


# blueprint routes
# normal routes

from app import app

app.secret_key = "Testing123"


@app.route("/")
@app.route("/index")
def index():
    try:
        current_user_id = session["user_id"]
        user = get_user(user_id=current_user_id)
    except KeyError:
        user = [201, "No one logged in"]

    posts = get_all_posts()

    for post in posts:
        print(post)

    return render_template("index.html", posts=posts, user=user)


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


@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user_id", None)
    return redirect("login")


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        user_id = session["user_id"]
        add_post(title, content, user_id)

        return redirect(url_for("index"))

    return render_template("create_post.html")
