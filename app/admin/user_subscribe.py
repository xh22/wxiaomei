# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect

from main import app, db

class Admin_user_subscribe(MethodView):

    def get(self):
        length = request.args["length"]
        start = request.args["start"]
        search = request.args['search[value]']
        cur = db.connection.cursor()
        if search:
            cur.execute("""select title, email, type, FROM_UNIXTIME(start, '%Y-%m-%d--%T' ), 
                       FROM_UNIXTIME(end, '%Y-%m-%d--%T' ), create_time from subscribe_calendar 
                       where title='{2}' order by create_time desc
                       limit {0}, {1}""".format(start, length, search))
        else:
            cur.execute("""select title, email, type, FROM_UNIXTIME(start, '%Y-%m-%d--%T' ), 
                       FROM_UNIXTIME(end, '%Y-%m-%d--%T' ),
                       create_time from subscribe_calendar order by create_time desc
                       limit {}, {}""".format(start, length))
        info = cur.fetchall()
        info = [[str(j) for j in i] for i in info]
        return json.dumps({"data": info})
            
app.add_url_rule('/admin/user_subscribe', view_func=Admin_user_subscribe.as_view('admin_user_subscribe'))
