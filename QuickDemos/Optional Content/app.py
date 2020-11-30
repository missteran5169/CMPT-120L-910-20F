from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Switching to the Index Page")
    return render_template('index.html')

@app.route('/home')
def home():
    app.logger.info("Switching to the Home Page")
    return render_template('home.html')

@app.route('/about')
def about():
    app.logger.info("Switching to the About Page")
    return render_template('about.html')

@app.route('/personality')
def personality():
    app.logger.info("Switching to the Personality Page")
    return render_template('personality.html')

@app.route('/404')
def four_oh_four():
    app.logger.info("Switching to the 404 Page, This is a test page so we don't need to error here.")
    return render_template('four_oh_four.html')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.warning("Switching to the 404 Page")
    return render_template('four_oh_four.html'), 404