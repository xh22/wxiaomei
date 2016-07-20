# -*- coding: utf-8 -*-
import random, json
from flask import session, render_template, request, redirect
from flask.views import MethodView

from main import app, db
from unity import msg

class VerifyMsg(MethodView):

    def post(self):
        code = "".join([str(random.randint(0, 9)) for i in range(0, 4)])
        phonenum = request.form['phonenum']
        msg.sendsms(phonenum, code)
        session["verifycode"] = code
        return json.dumps({"success": True})

app.add_url_rule('/verify/msg', view_func=VerifyMsg.as_view('verifymsg'))
