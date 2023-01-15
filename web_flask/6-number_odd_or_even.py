#!/usr/bin/python3

""" Hello Flask """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """hello Hbnb returns"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """hello Hbnb returns"""
    return 'HBNB'


@app.route('/c/<text>')
def clove(text):
    """C is Fun """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def py(text="is cool"):
    """C is Fun """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def num(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    v = "is odd"
    if n % 2 == 0:
        v = "is even"

    return render_template('6-number_odd_or_even.html', n=n, v=v)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
