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
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/login')
def login():
    try:
        return render_template('login.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/work')
def work():
    try:
        return render_template('work.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/service')
def service():
    try:
        return render_template('service.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/news')
def news():
    try:
        return render_template('news.html')
    except TemplateNotFound:
        abort(404)

@index_page.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except TemplateNotFound:
        abort(404)

app.register_blueprint(index_page)
