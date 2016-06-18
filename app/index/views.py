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


@index_page.route('/subscribe/<int:page>')
def subscribe(page):
    if not session.get('logged_in', None) and page != 0:
        return redirect('/subscribe/0')
    else:
        try:
            return render_template('subscribe/subscribe%s.html' % page)
        except TemplateNotFound:
            abort(404)

app.register_blueprint(index_page)
