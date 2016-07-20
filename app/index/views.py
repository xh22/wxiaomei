import os

from flask import Blueprint, render_template, abort, session, redirect
from jinja2 import TemplateNotFound

from main import app

index_page = Blueprint('index_page', __name__,
                        template_folder='templates',
                      )

@index_page.route('/', defaults={'page': 'index'})
@index_page.route('/<string:page>')
def index(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

@index_page.route('/news')
def news():
    videos = map(lambda x: x[2], os.walk(os.path.join(app.root_path, 'static/video')))	
    videos = map(lambda x: x.split("."), videos[0])
    return render_template('news.html', videos=videos)
        
@index_page.route('/videos/<string:ids>/<string:types>')
def videos(ids, types):
    return render_template('video.html', ids=ids, types=types)

@index_page.route('/work')
def work():
    imgs0 = os.listdir(os.path.join(app.root_path, 'static/img/portfolio/0'))
    imgs1 = os.listdir(os.path.join(app.root_path, 'static/img/portfolio/1'))
    imgs2 = os.listdir(os.path.join(app.root_path, 'static/img/portfolio/2'))
    imgs3 = os.listdir(os.path.join(app.root_path, 'static/img/portfolio/3'))
    return render_template('work.html', imgs=[imgs0, imgs1, imgs2, imgs3], enumerate=enumerate)

@index_page.route('/subscribe/<int:page>')
def subscribe(page):
    if page != 1:
        if not session.get('subscribe_type', None):
            return redirect('/subscribe/1')
    else:
        try:
            return render_template('subscribe/subscribe%s.html' % page)
        except TemplateNotFound:
            abort(404)

app.register_blueprint(index_page)
