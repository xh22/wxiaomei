# -*- coding: utf-8 -*-
import os

from flask import session, render_template, request, redirect
from flask.views import MethodView

from main import app, db

class Login(MethodView):

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""select name,password from user_info where email="{}";""".format(request.form['email']))
        psw = cur.fetchone()
        if not psw:
            error = u'没有此用户'
        elif request.form['password'] != psw[1]:
            error = u'密码错误'
        else:
            session['logged_in'] = True
            session['email'] = request.form['email']
            session['name'] = psw[0]
        return redirect('/')            


app.add_url_rule('/login', view_func=Login.as_view('login'))
