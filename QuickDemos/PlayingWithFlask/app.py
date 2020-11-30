import logging
from flask import Flask
from flask import render_template

app = Flask(__name__)
# Logger level is default logging.WARNING
app.logger.setLevel(logging.INFO)

@app.route('/')
def index():
    app.logger.info("User traveled to the info route.")
    return render_template("index.html")

@app.route('/hello')
def hello_world():
    app.logger.warning("This page isn't finished yet but we say hello.")
    return 'Hello, ME!'