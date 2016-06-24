import os
from datetime import timedelta

from flask import Flask
from flask_mysql import Mysql
from flask.ext.session import Session

app = Flask(__name__)
SESSION_TYPE = 'redis'
ADMIN_EMAIL = 'admin@qq.com'
UPLOADED_PHOTOS_DEST = os.path.join(app.root_path, 'static/img')
UPLOADED_VIDEOS_DEST = os.path.join(app.root_path, 'static/video')
PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

app.config.from_object(__name__)
app.secret_key = os.urandom(24)

db = Mysql(app)
Session(app)

import views
