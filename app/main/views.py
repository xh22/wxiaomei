from flask import session, request, redirect

from main import app

@app.before_request
def before_request():
    pass
#    if '/static' not in request.path:
#        if request.path not in ['/', '/login', '/regist', 'logout']:
#            if not session.get('logged_in', None):
#                return redirect('/')
