from flask import Blueprint, render_template, session, redirect, url_for

index_bp = Blueprint('index_bp', __name__, template_folder='templates')

@index_bp.route('/')
def index():
    if session.get('user_id'):
        return redirect(url_for('user_bp.get_user_repos', page=1))
    return render_template('index.html')
