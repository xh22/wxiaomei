# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash
from flask_mail import Message

from main import app, db, mail
from unity import auth_token 

class Regist(MethodView):

    def post(self):
        if request.form["repassword"] != request.form["password"]:
            flash(u"两次输入密码不一致!")
            return redirect('/regist')
        mail_html = open(os.path.join(app.root_path, 'static/mail/email.html')).read()
        url = auth_token.Auth_token.generate_auth_token(json.dumps(request.form))
        msg = Message(u'明天工作室', recipients=[request.form["email"]])
        msg.html = mail_html.replace('{}', url) 
        mail.send(msg)
        return redirect('/regist')

class Regist_done(MethodView):

    def get(self):
        token = request.args["token"]
        form = auth_token.Auth_token.verify_auth_token(token)
        if form:
            form = json.loads(form)
            cur = db.connection.cursor()
            cur.execute("""insert into user_info (name, phone, email,  password, address)
                values("{}", "{}", "{}", "{}", "{}");""".format(form['name'], form['phone'],
                form['email'], form['password'], form['address']))
            db.connection.commit()
            session['logged_in'] = True
            session['email'] = form['email']
            session['name'] = form['name']
            return redirect('/')

class Forget_password(MethodView):

    def post(self):
        cur = db.connection.cursor()
        cur.execute("""select password from user_info where email="{}";""".format(request.form['email']))
        password = cur.fetchone()
        if password:
            mail_html = open(os.path.join(app.root_path, 'static/mail/email_password.html')).read()
            msg = Message(u'明天工作室', recipients=[request.form["email"]])
            msg.html = mail_html.replace('{}', password[0]) 
            mail.send(msg)
        return redirect('/')

app.add_url_rule('/regist', view_func=Regist.as_view('regist'))
app.add_url_rule('/regist/done', view_func=Regist_done.as_view('regist_done'))
app.add_url_rule('/forget_password', view_func=Forget_password.as_view('forget_password'))
