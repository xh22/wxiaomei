# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect

from main import app, db

class Admin_subscribe_type(MethodView):

    def get(self, typer):
        session['subscribe_type'] = typer
        return redirect('/admin/subscribe/2')

class Admin_subscribe_calendar(MethodView):

    def get(self):
        cur = db.connection.cursor()
        cur.execute("""select start, end, title from subscribe_calendar where type="{}"
            """.format(session['subscribe_type']))
        info = cur.fetchall()
        return json.dumps({"success": True, "event": info, "type": session['subscribe_type']}) 
            

app.add_url_rule('/admin/subscribe/calendar', view_func=Admin_subscribe_calendar.as_view('admin_subscribe_calendar'))
app.add_url_rule('/admin/subscribe/type/<int:typer>', view_func=Admin_subscribe_type.as_view('admin_subscribe_type'))
