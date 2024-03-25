#!/usr/bin/python3
"""
starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
    /: displays “Hello HBNB!”
    /hbnb: displays “HBNB”
    /c/<text>: displays “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    /python/(<text>): displays “Python ” followed by value of the text variable
        (replace underscore _ symbols with a space )
        The default value of text is “is cool”
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_C(text):
    """returns C followed by value of text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_Python(text='is cool'):
    """returns Python followed by value of text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """returns “n is a number”"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
