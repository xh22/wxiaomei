# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect

from main import app, db

class Admin_user_info(MethodView):

    def get(self):
        length = request.args["length"]
        start = request.args["start"]
        cur = db.connection.cursor()
        cur.execute("""select name, phone, address, password, email,
                       create_time from user_info limit {}, {}""".format(start, length))
        info = cur.fetchall()
        info = [[str(j) for j in i] for i in info]
        return json.dumps({"data": info})
            
app.add_url_rule('/admin/user_info', view_func=Admin_user_info.as_view('admin_user_info'))
