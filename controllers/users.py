from flask import Blueprint, session, url_for, redirect, jsonify, render_template
from app import github

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/user/repos/')
def get_user_repos():
    user = github.get('user')
    username = user['login']
    results = github.get('users/'+username+'/repos')
    return render_template('repositories.html', 
                           results=results, owner=username)

@user_bp.route('/user/commits/<owner>/<repo>/')
def get_user_repos_commits(owner, repo):
    commits = github.get('repos/'+owner+'/'+repo+'/commits')
    return jsonify(results=commits)

@user_bp.route('/user/login/')
def login():
    if session.get('user_id', None) is None:
        return github.authorize()
    else:
        return 'Already logged in'

@user_bp.route('/user/logout/')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index_bp.index'))