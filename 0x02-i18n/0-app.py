#!/usr/bin/env python3
"""
This module contains a Flask application that serves a welcome page.

The application uses the Flask framework to create a web server
and render an HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    """
    Renders the welcome page.

    Returns:
        The rendered HTML template for the welcome page.
    """

    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
