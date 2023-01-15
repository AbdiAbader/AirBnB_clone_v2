#!/usr/bin/python3

""" Hello Flask """

from flask import Flask

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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
