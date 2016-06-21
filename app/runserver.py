import index
from main import app as application 
from datetime import timedelta

app = application
app.permanent_session_lifetime = timedelta(minutes=60)

if __name__ == '__main__':
    app.run(host="120.25.171.88",debug=True, use_reloader=True)
