from . import db


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    is_completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Task {self.title}, {self.is_completed}>"
