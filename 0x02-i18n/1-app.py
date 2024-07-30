#!/usr/bin/env python3
"""
This module contains a Flask application that supports
internationalization (i18n).
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


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
