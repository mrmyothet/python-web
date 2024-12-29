from flask import Flask, render_template, Blueprint
from . import db
from .models import Task

# app = Flask(__name__)
bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)
