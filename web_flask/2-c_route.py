#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """return simple text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """return hbnb"""
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    """return with var value"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
