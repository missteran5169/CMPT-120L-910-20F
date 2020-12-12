from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Switching to the Index page")
    return render_template("index.html")

@app.route('/about')
def about():
    app.logger.info("Switching to the About page")
    return render_template("about.html")

@app.route('/resume')
def rentals():
    app.logger.info("Switching to the Resume page")
    return render_template("resume.html")

@app.route('/home')
def home():
    app.logger.info("Switching to the Home page")
    return render_template("home.html")

@app.route('/404')
def four_oh_four():
    app.logger.info("Switching to the Index page, this is a test page so we dont need to error here.")
    return render_template("four_oh_four.html")

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning("Switching to the 404 page")
    return render_template('four_oh_four.html'), 404

if __name__ == "__main__":
    app.run(debug=True)