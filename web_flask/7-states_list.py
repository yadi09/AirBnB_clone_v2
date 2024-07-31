#!/usr/bin/python3
"""script that starts a Flask web application:"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list')
def stateList():
    states = [list for list in storage.all(State).values()]
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
