#!/usr/bin/env python3
"""
This module contains a Flask application that supports
internationalization (i18n).
"""

from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """
    Get the best matching language locale based on the user's preferences.

    Returns:
        str: The best matching language locale.
    """

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    Get the user based on the 'login_as' query parameter.

    Returns:
        User object: The user corresponding to the 'login_as' query parameter.
                    None if the 'login_as' query parameter is not
                    provided or is not a valid integer.
    """

    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """
    This function is a Flask before_request decorator
    that is executed before each request.
    It sets the `g.user` variable to the current user
    by calling the `get_user()` function.
    """

    g.user = get_user()


@app.route('/')
def welcome():
    """
    Renders the welcome page.

    Returns:
        The rendered HTML template for the welcome page.
    """

    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
