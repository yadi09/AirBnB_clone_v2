#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)
"""app flask"""
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exception):
    """tear down"""
    storage.close()


@app.route("/hbnb_filters")
def hbnb_filter():
    """route hbnb"""
    all_state = list(storage.all(State).values())
    all_ameni = list(storage.all(Amenity).values())
    all_state.sort(key=lambda s: s.name)
    all_ameni.sort(key=lambda a: a.name)
    for state in all_state:
        state.cities.sort(key=lambda c: c.name)

    all_data = {'state': all_state, 'amenities': all_ameni}

    return render_template('10-hbnb_filters.html', **all_data)

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port="5000")
