import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('index.html', **temp_data)


@app.route('/indeed_scraper')
def indeed_scraper():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('indeed.html', **temp_data)


@app.route('/overstock_scraper')
def overstock_scraper():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('overstock.html', **temp_data)


@app.route('/bed_bath_and_beyond')
def bed_bath_and_beyond():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('bed_bath_and_beyond.html', **temp_data)


@app.route('/google_news')
def google_news():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('google_news.html', **temp_data)


@app.route('/home_depot')
def home_depot():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('home_depot.html', **temp_data)


@app.route('/samsclub')
def samsclub():
    temp_data = {'title': 'Scrap_utils'}
    return render_template('samsclub.html', **temp_data)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
