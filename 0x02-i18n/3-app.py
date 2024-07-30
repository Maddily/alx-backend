#!/usr/bin/env python3
"""
This module contains a Flask application that supports
internationalization (i18n).
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Get the best matching language locale based on the user's preferences.

    Returns:
        str: The best matching language locale.
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome() -> str:
    """
    Renders the welcome page.

    Returns:
        The rendered HTML template for the welcome page.
    """

    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
