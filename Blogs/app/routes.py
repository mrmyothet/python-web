from flask import Flask, render_template, request, redirect, url_for, session
from app.models import create_user


# blueprint routes
# normal routes

from app import app


@app.route("/")
def index():
    posts = "Posts"
    return render_template("index.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        create_user(username, password, email)

        return "Register Successful"

    if request.method == "GET":
        return render_template("register.html")
