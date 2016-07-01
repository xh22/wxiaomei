# -*- coding: utf-8 -*-

import StringIO

from flask import session, render_template, request, redirect
from flask.views import MethodView

from main import app, db
from unity import verify_code

class Verify(MethodView):

    def get(self, arg):
        code, img = verify_code.get_verify_pic()
        session["verify_code"] = code
        buf = StringIO.StringIO()
        img.save(buf, 'png')
        buf_str = buf.getvalue()
        response = app.make_response(buf_str)
        response.headers['Content-Type'] = 'image/png'
        return response

app.add_url_rule('/verify/<int:arg>', view_func=Verify.as_view('verify'))
