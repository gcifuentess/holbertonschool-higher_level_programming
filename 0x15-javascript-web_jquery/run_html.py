#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from sys import argv
app = Flask(__name__, template_folder='', static_folder='')


@app.route('/', strict_slashes=False)
def index():
    return render_template(argv[1])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
