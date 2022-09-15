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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """list of all State objects present in DBStorage sorted by name (A->Z)"""
    states_lst = storage.all(State)
    return render_template("7-states_list.html", states_lst=states_lst)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
