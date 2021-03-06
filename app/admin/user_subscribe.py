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
            cur.execute("""select title, type, FROM_UNIXTIME(start, '%Y-%m-%d--%T' ), 
                       FROM_UNIXTIME(end, '%Y-%m-%d--%T' ), create_time from subscribe_calendar 
                       where title like '%{2}%' order by end
                       limit {0}, {1}""".format(start, length, search.encode('utf8')))
        else:
            cur.execute("""select title, type, FROM_UNIXTIME(start, '%Y-%m-%d--%T' ), 
                       FROM_UNIXTIME(end, '%Y-%m-%d--%T' ),
                       create_time from subscribe_calendar where LENGTH(title)>1 order by end
                       limit {}, {}""".format(start, length))
        info = cur.fetchall()
        info = [[str(j) for j in i] for i in info]
        return json.dumps({"data": info})
            
app.add_url_rule('/admin/user_subscribe', view_func=Admin_user_subscribe.as_view('admin_user_subscribe'))
