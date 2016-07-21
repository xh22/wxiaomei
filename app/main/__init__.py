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
UPLOADED_VIDEOPIC_DEST = os.path.join(app.root_path, 'static/img/video/')

ADMIN_EMAIL = 'admin@qq.com'

MAIL_SERVER = "smtp.qq.com"
MAIL_USERNAME = "910192724" 
MAIL_PASSWORD = "kztzbamoukxebbhg"
MAIL_DEFAULT_SENDER = "910192724@qq.com"
MAIL_USE_TLS = True

app.config.from_object(__name__)
#app.secret_key = os.urandom(24)
app.secret_key = "\xd7N\x97\xce\xa0'\xf6\xbb8m\x19\xb5\x15\x97\x8d\xfdk\x98\x9a\x02)i\x0c\xa1"

db = Mysql(app)
mail = Mail(app)
Session(app)

import views
