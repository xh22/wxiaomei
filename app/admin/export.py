# -*- coding: utf-8 -*-

from flask.views import MethodView
from flask import session, render_template, request, redirect
from flask.ext import excel

from main import app, db

class Export(MethodView):

    def get(self):
        cur = db.connection.cursor()
        cur.execute("""select title, FROM_UNIXTIME(start, '%Y-%m-%d--%T' ), 
                   FROM_UNIXTIME(end, '%Y-%m-%d--%T' )
                   from subscribe_calendar where 
                   month(FROM_UNIXTIME(start, '%Y-%m-%d--%T' )) < 
                   month(localtime())""")
        info = cur.fetchall()
        return excel.make_response_from_array(info, "csv")
            
app.add_url_rule('/admin/export', view_func=Export.as_view('admin_export'))
