import os

from flask import Flask
from flask_mysql import Mysql

app = Flask(__name__)
app.secret_key = os.urandom(24)

db = Mysql(app)

import views
