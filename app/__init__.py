"""
Authorize Users and fetch commit logs
"""
from flask import Flask, request, g, session, redirect, url_for
from flask import render_template_string
from flask.ext.github import GitHub
from helpers.jinja2_env_filters import datetimeformat
from models.tables import User
from models.db_connection import db_session
from helpers.config_reader import (DEBUG, SECRET_KEY, GITHUB_CLIENT_ID,
                                   GITHUB_CLIENT_SECRET)

# setup flask
app = Flask(__name__)
app.config.from_object(__name__)

# jinja2 filter
app.jinja_env.filters['datetimeformat'] = datetimeformat

# setup github-flask
github = GitHub(app)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.after_request
def after_request(response):
    db_session.remove()
    return response

@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user.github_access_token

import controllers
