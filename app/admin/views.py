import os

from flask import Blueprint, render_template, abort, session, redirect
from jinja2 import TemplateNotFound

from main import app

admin_page = Blueprint('admin_page', __name__,
                        template_folder='templates',
                      )

@admin_page.route('/admin', defaults={'page': 'index'})
@admin_page.route('/admin/<string:page>')
def admin(page):
    try:
        return render_template('admin_%s.html' % page)
    except TemplateNotFound:
        abort(404)

@admin_page.route('/admin/subscribe/<int:page>')
def subscribe(page):
    try:
        return render_template('admin_subscribe%s.html' % page)
    except TemplateNotFound:
        abort(404)

app.register_blueprint(admin_page)
