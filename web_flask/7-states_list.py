#!/usr/bin/python3
"""
starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
   /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
    sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """ After each request remove the current SQLAlchemy """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """ display a HTML page"""
    print(storage.all("State"))
    return render_template('7-states_list.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
