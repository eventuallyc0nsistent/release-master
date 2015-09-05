from flask import Blueprint, request, url_for, redirect, session
from models.tables import User
from models.db_connection import db_session
from app import github

ghub_bp = Blueprint('ghub_bp', __name__, template_folder='templates')

@ghub_bp.route('/gh/callback')
@github.authorized_handler
def authorized(access_token):
    next_url = request.args.get('next') or url_for('index_bp.index')
    if access_token is None:
        return redirect(next_url)

    user = User.query.filter_by(github_access_token=access_token).first()
    if user is None:
        user = User(access_token)
        db_session.add(user)
    user.github_access_token = access_token
    db_session.commit()

    session['user_id'] = user.id
    return redirect(next_url)