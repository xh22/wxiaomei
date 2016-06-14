from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from main import app

index_page = Blueprint('index_page', __name__,
                        template_folder='templates')

@index_page.route('/', defaults={'page': 'index'})
@index_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

app.register_blueprint(index_page)
