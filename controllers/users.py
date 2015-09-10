import re
from app import github
from flask import (Blueprint, session, url_for, jsonify,
                   redirect, render_template, request)

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/user/repos/<page>', defaults={'page': 1})
@user_bp.route('/user/repos/<int:page>')
def get_user_repos(page):
    response = github.raw_request('get', 'user/repos?page=%s'%page)
    json_ = response.json()
    pages = get_pages(response.links)

    return render_template('repositories.html',
                           repos=json_,
                           pages=pages,
                           current_page=page,
                           title='Public + Private Repos')

def get_pages(response_link):

    # gh defines the page link headers for these values
    page_names = ['next', 'last', 'prev', 'first']

    pages = {}
    for pg_name in page_names:
        url = response_link.get(pg_name)
        if url:
            match = re.match(r'.*page=(\d+)&access', url['url'])
            pg_num = match.group(1)
            pages[pg_name] = pg_num
    return pages

@user_bp.route('/user/commits/<owner>/<repo>/<page>', defaults={'page': 1})
@user_bp.route('/user/commits/<owner>/<repo>/<int:page>')
def get_user_repos_commits(owner, repo, page):
    response = github.raw_request(
                'get', 'repos/'+owner+'/'+repo+'/commits?page=%s'%page)
    json_ = response.json()
    pages = get_pages(response.links)
    # return jsonify(result=json_)
    return render_template('commit-messages.html',
                           pages=pages,
                           current_page=page,
                           results=json_,
                           owner=owner,
                           repository=repo,
                           title='Commits')

@user_bp.route('/user/add-to-changelog/<commit_hash>')
def add_to_changelog(commit_hash):
    print commit_hash
    return jsonify(result=True)

@user_bp.route('/user/login')
def login():
    if session.get('user_id', None) is None:
        return github.authorize(scope='repo,user:email')
    return 'Already logged in'

@user_bp.route('/user/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index_bp.index'))
