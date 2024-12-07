from flask import Flask

app = Flask(__name__)
app.secret_key = "TestingKey"

from app import routes
