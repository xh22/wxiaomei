import index, admin

from main import app as application 

app = application

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
