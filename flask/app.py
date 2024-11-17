from flask import Flask, render_template

app = Flask(__name__)


# MVT - Model View Template 
# view function 
# request and response 
@app.route("/")
def hello_world():
    return "<p>Hello World from Flask</p>"

@app.route("/contact-us")
def contact_us():
    return render_template('contact-us.html')

@app.route("/about-us")
def about_us():
    return render_template('/about/about-us.html')

