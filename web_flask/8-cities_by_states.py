#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
""" app flask """
@app.teardown_appcontext
def tear_down(exception):
    """teardown"""
    storage.close()


@app.route("/cities_by_states")
def cityByState():
    """city by state"""
    state_by_city = storage.all(State).values()
    sorted_data = sorted(state_by_city, key=lambda sc: sc.name)
    return render_template('8-cities_by_states.html', data=sorted_data)

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port="5000", debug=True)
