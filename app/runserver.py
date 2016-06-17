import index
from main import app as application 

app = application

if __name__ == '__main__':
    app.run(debug=True, host="120.25.171.88", port=8888, use_reloader=True)
