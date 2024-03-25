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
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
    h1 tag: “Number: n” inside the tag body

"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """returns a HTML page only if n is an intege”"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
