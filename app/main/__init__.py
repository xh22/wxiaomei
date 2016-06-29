import os
from datetime import timedelta

from flask import Flask
from flask_mysql import Mysql
from flask_mail import Mail
from flask.ext.session import Session

app = Flask(__name__)
SESSION_TYPE = 'redis'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

UPLOADED_PHOTOSCERT_DEST = os.path.join(app.root_path, 'static/img/portfolio/0/')
UPLOADED_PHOTOSPORT_DEST = os.path.join(app.root_path, 'static/img/portfolio/1/')
UPLOADED_VIDEOS_DEST = os.path.join(app.root_path, 'static/video/')

ADMIN_EMAIL = 'admin@qq.com'

MAIL_SERVER = "smtp.qq.com"
MAIL_USERNAME = "910192724" 
MAIL_PASSWORD = "qaz123!"
MAIL_DEFAULT_SENDER = "910192724@qq.com"
MAIL_USE_TLS = True

app.config.from_object(__name__)
app.secret_key = os.urandom(24)

db = Mysql(app)
mail = Mail(app)
Session(app)

import views
