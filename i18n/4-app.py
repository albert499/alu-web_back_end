#!/usr/bin/env python3
"""Flask app with i18n support and locale forcing via URL parameter"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Flask Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages
    Priority:
    1. Locale from URL parameters
    2. Locale from request headers
    """
    # Check if locale parameter is in the URL
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # Fall back to best match from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
