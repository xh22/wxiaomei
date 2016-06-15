import os

from flask import Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound

from main import app

index_page = Blueprint('index_page', __name__,
                        template_folder='templates',
                      )

@index_page.route('/')
def index():
    try:
        if session.get('logged_in', None):
            return render_template('index.html')
        else:
            return render_template('login.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/login')
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/regist')
def regist():
    try:
        return render_template('regist.html')
    except TemplateNotFound:
        abort(404)

app.register_blueprint(index_page)
