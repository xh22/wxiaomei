import MySQLdb 

from contextlib import closing

from main import app

def connect_db():
    return MySQLdb.connect(host='localhost', user='root', passwd='', db='users', port=3306)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().execute(f.read())
        db.commit()

init_db()
