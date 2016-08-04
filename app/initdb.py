# -*- coding: utf-8 -*-
import MySQLdb 

from contextlib import closing

from main import app

def connect_db():
    return MySQLdb.connect(host='localhost', user='root', passwd='qaz123', db='users', port=3306)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().execute(f.read())
        db.commit()

def exec_db():
    with closing(connect_db()) as db:
        a=1469116800
        for i in range(0,48*30):
            b=a+1800
            db.cursor().execute("""insert into subscribe_calendar(start, end, title, type) values("{0}", "{1}", "-", "0")""".format(a,b))
            a=b
        db.commit()

def insert_db():
    with closing(connect_db()) as db:
        db.cursor().execute(""" insert into product_type (type ,description) values(1,"证件照") """)
        db.cursor().execute(""" insert into product_type (type ,description) values(2,"轻写真") """)
        db.cursor().execute(""" insert into product_type (type ,description) values(3,"Happy Face 系列") """)
        db.commit()


def event():
    sql="""
set global event_scheduler=1;
create event myevent on schedule
every 1 day starts '2016-07-19 00:00:00'
do call subscribe()
"""
    with closing(connect_db()) as db:
        db.cursor().execute(sql)
        db.commit()

def proc():
    sql="""
create procedure subscribe()
begin
declare i int;
set i=0;
while i<48 do
    insert into subscribe_calendar(start, end, title, type) values(
    unix_timestamp(now())+3600*24*29+1800*i, unix_timestamp(now())+3600*24*29+1800*(i+1), "", "0");
    set i=i+1;
end while;
end;
"""
    with closing(connect_db()) as db:
        db.cursor().execute(sql)
        db.commit()
#delete from subscribe_calendar where SYSDATE()>FROM_UNIXTIME(end);
#select * from mysql.event
#drop event myevent
#show create procedure subscribe
#drop procedure subscribe
#insert into product_type (type ,description) values(1,"证件照");
#insert into user_info (name, phone , password ,email) values ("admin", 0 ,123,"admin@qq.com");
#init_db()
exec_db()
#insert_db()
proc()
#event()
