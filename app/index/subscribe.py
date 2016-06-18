# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect

from main import app, db

class Subscribe_type(MethodView):

    def get(self, typer):
        session['subscribe_type'] = typer
        return redirect('/subscribe/2')

class Subscribe_calendar(MethodView):

    def get(self):
        cur = db.connection.cursor()
        cur.execute("""select start, end, title from subscribe_calendar where email="{}" and type="{}"
            """.format(session['email'], session['subscribe_type']))
        info = cur.fetchall()
        return json.dumps({"success": True, "event": info}) 

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""insert into subscribe_calendar(email, start, end, title, type)
            values("{}", "{}", "{}", "{}", "{}");""".format(session['email'], request.form['start'],
            request.form['end'], request.form['title'].encode("utf-8"), session['subscribe_type']))
        db.connection.commit()
        return json.dumps({"success": True}) 

class Subscribe_login(MethodView):

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""select password from user_info where email="{}";""".format(request.form['email']))
        psw = cur.fetchone()
        if not psw:
            error = u'没有此用户'
        elif request.form['password'] != psw[0]:
            error = u'密码错误'
        else:
            session['logged_in'] = True
            session['email'] = request.form['email']
        return redirect('/subscribe/1')            

app.add_url_rule('/subscribe/login', view_func=Subscribe_login.as_view('subscribe_login'))
app.add_url_rule('/subscribe/calendar', view_func=Subscribe_calendar.as_view('subscribe_calendar'))
app.add_url_rule('/subscribe/type/<int:typer>', view_func=Subscribe_type.as_view('subscribe_type'))
