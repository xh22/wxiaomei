# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash, abort

from main import app, db

class Subscribe_type(MethodView):

    def get(self, typer):
        cur = db.connection.cursor()
        cur.execute("""select type,description from product_type;""")
        info = cur.fetchall()
        session['subscribe_type'] = dict(info)[typer]
        return redirect('/subscribe/2')

class Subscribe_calendar(MethodView):

    def get(self):
        cur = db.connection.cursor()
        cur.execute("""select start, end, title from subscribe_calendar where
            end > unix_timestamp(now())""")
        info = cur.fetchall()
        return json.dumps({"success": True, "event": info, "type": session['subscribe_type']}) 

    def post(self):
        if request.form['verifycode'] != session.get('verifycode', None):
            abort(401) 
        cur = db.connection.cursor()
        cur.execute("""update subscribe_calendar set title=concat(title,"{3}-{1}-{2},") where start="{0}"
            ;""".format(request.form['start'], request.form['phonenum'], session['subscribe_type'],
            request.form['name'].encode('utf8')))
        db.connection.commit()
        return json.dumps({"success": True}) 
            

class Subscribe_login(MethodView):

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""select name,password from user_info where email="{}";""".format(request.form['email']))
        psw = cur.fetchone()
        if not psw:
            flash(u'没有此用户')
            return redirect('/subscribe/0')            
        elif request.form['password'] != psw[1]:
            flash(u'密码错误')
            return redirect('/subscribe/0')            
        else:
            session['logged_in'] = True
            session['email'] = request.form['email']
            session['name'] = psw[0]
        return redirect('/subscribe/1')            

app.add_url_rule('/subscribe/login', view_func=Subscribe_login.as_view('subscribe_login'))
app.add_url_rule('/subscribe/calendar', view_func=Subscribe_calendar.as_view('subscribe_calendar'))
app.add_url_rule('/subscribe/type/<int:typer>', view_func=Subscribe_type.as_view('subscribe_type'))
