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
def ctext(text):
    """return with var value"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def pytext(text):
    """py text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def display_int(n):
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
