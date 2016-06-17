# -*- coding: utf-8 -*-
import os

from flask.views import MethodView
from flask import session, render_template, request, redirect

from main import app, db

class Regist(MethodView):

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""insert into user_info (name, phone, email,  password, address)
            values("{}", "{}", "{}", "{}", "{}");""".format(request.form['name'], request.form['phone'],
            request.form['email'], request.form['password'], request.form['address']))
        db.connection.commit()
        session['logged_in'] = True
        return redirect('/')

app.add_url_rule('/regist', view_func=Regist.as_view('regist'))
