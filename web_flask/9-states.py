#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """display a HTML page: (inside the tag BODY"""
    states_lst = storage.all(State)
    return render_template("9-states.html", states_lst=states_lst)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    """display a HTML page: (inside the tag BODY"""
    key = "State." + str(id)
    if key in storage.all(State):
        state = storage.all()[key]
    else:
        state = None
    return render_template("9-states.html", state=state)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
