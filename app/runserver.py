import index
from main import app as application 
from datetime import timedelta
from flask.ext.session import Session

app = application
SESSION_TYPE = 'redis'
PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
app.config.from_object(__name__)
Session(app)

#app.permanent_session_lifetime = timedelta(minutes=60)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
