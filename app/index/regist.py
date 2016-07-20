# -*- coding: utf-8 -*-
import os, json

from flask.views import MethodView
from flask import session, render_template, request, redirect, flash
from flask_mail import Message

from MySQLdb import IntegrityError
from jwt import DecodeError 

from main import app, db, mail
from unity import auth_token 

class Regist(MethodView):

    def post(self):
        if request.form["repassword"] != request.form["password"]:
            flash(u"两次输入密码不一致!")
            return redirect('/regist')
        elif request.form["verify_code"] != session["verify_code"]:
            flash(u"验证码错误!")
            return redirect('/regist')
        mail_html = open(os.path.join(app.root_path, 'static/mail/email_regist.html')).read()
        url = auth_token.Auth_token.generate_auth_token(request.form)
        msg = Message(u'明天工作室', recipients=[request.form["email"]])
        msg.html = mail_html.replace('{}', url) 
        mail.send(msg)
        flash(u"已发送验证链接到您的邮箱,请登录您的邮箱完成注册!")
        return redirect('/regist')

class Regist_done(MethodView):

    def get(self):
        token = request.args.get("token", None)
        if not token:
            return redirect('/regist')
        try:
            form = auth_token.Auth_token.verify_auth_token(token)
        except DecodeError as e:
            flash(u"注册失败")
            return redirect('/regist')
        if form:
            cur = db.connection.cursor()
            try:
                cur.execute("""insert into user_info (name, phone, email, password)
                    values("{}", "{}", "{}", "{}", "{}");""".format(form['name'][0], form['phone'][0],
                    form['email'][0], form['password'][0]))
            except IntegrityError:
                flash(u"用户已存在!")
                return redirect('/regist')
            db.connection.commit()
            session['logged_in'] = True
            session['email'] = form['email'][0]
            session['name'] = form['name'][0]
        return redirect('/')


class Forget_password(MethodView):

    def get(self):
        return render_template('forget_password.html')

    def post(self):
        if request.form["verify_code"] != session["verify_code"]:
            flash(u"验证码错误!")
            return redirect('/password/forget')
        cur = db.connection.cursor()
        cur.execute("""select email from user_info where email="{}";""".format(request.form['email']))
        email = cur.fetchone()
        if email:
            mail_html = open(os.path.join(app.root_path, 'static/mail/email_password.html')).read()
            msg = Message(u'明天工作室', recipients=[request.form["email"]])
            url = auth_token.Auth_token.generate_auth_token({"email": email[0]})
            msg.html = mail_html.replace('{}', url) 
            mail.send(msg)
            flash(u"请登录您的邮箱获取重置链接!")
            return redirect('/password/forget')
        else:
            flash(u"用户不存在!")
            return redirect('/password/forget')

class Reset_password(MethodView):

    def get(self):
        if session.get('email', None):
            return render_template('reset_password.html')
        token = request.args.get("token", None)
        if not token:
            return redirect('/password/forget')
        try:
            form = auth_token.Auth_token.verify_auth_token(token)
        except DecodeError as e:
            flash(u"密码重置失败")
            return redirect('/password/forget')
        
        session['email'] = form['email']
        return render_template('reset_password.html')

    def post(self):
        if request.form["repassword"] != request.form["password"]:
            flash(u"两次输入密码不一致!")
            return redirect('/password/reset')
        cur = db.connection.cursor()
        cur.execute("""update user_info set password="{}" where email="{}";""".format(
            request.form['password'], session["email"]))
        cur.execute("""select name from user_info where email="{}";""".format(session['email']))
        name = cur.fetchone()
        db.connection.commit()
        session['logged_in'] = True
        session['name'] = name[0]
        return redirect('/')

app.add_url_rule('/regist', view_func=Regist.as_view('regist'))
app.add_url_rule('/regist/done', view_func=Regist_done.as_view('regist_done'))
app.add_url_rule('/password/forget', view_func=Forget_password.as_view('forget_password'))
app.add_url_rule('/password/reset', view_func=Reset_password.as_view('reset_password'))
