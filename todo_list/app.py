from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)
db.init()


@app.route("/")
def home():
    tasks = db.fetch_all_tasks()
    for task in tasks:
        # print(task["id"], task["description"], task["is_complete"])
        print(task[0], task[1], task[2])

    return render_template("index.html", list=tasks)


@app.route("/add-task", methods=["POST"])
def add_task():
    data = request.form["task_name"]
    if data:
        db.add_task(data)

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    db.delete_task(task_id)
    return redirect("/")
