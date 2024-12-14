# from flask import Flask
# app = create_app()

from app import app

if __name__ == "__main__":
    app.run(debug=True)
