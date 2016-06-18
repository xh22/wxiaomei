from flask import session, request, redirect, render_template

from main import app

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.before_request
def before_request():
    pass
#    if '/static' not in request.path:
#        if request.path not in ['/', '/login', '/regist', 'logout']:
#            if not session.get('logged_in', None):
#                return redirect('/')
