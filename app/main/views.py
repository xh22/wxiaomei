from flask import session, request, redirect, render_template, g

from main import app

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.before_request
def before_request():
    g.logged_in = bool(session.get('logged_in'))
    if request.path.startswith("/admin"):
        if not session.get('logged_in', None) or session.get('email', None) != app.config['ADMIN_EMAIL']:
            return redirect('/')
