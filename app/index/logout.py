# -*- coding: utf-8 -*-
import os

from flask import session, render_template, request, redirect
from flask.views import MethodView

from main import app, db

class Logout(MethodView):

    def get(self):
        session.pop('logged_in', None)
        return redirect('/login')

app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
