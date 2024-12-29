from flask import Flask, render_template, Blueprint, request, redirect, url_for
from . import db
from .models import Task

# app = Flask(__name__)
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    tasks = Task.query.all()
    print(tasks)
    return render_template("index.html", tasks=tasks)


@bp.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_task = Task(title=title)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/complete/<int:task_id>")
def complete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.is_completed = True
    db.session.commit()
    return redirect(url_for("main.index"))


@bp.route("/delete/<int:task_id>")
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("main.index"))
