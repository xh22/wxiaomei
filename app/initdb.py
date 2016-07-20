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
        a=1468944000
        for i in range(0,24*30):
            b=a+3600
            db.cursor().execute("""insert into subscribe_calendar(start, end, title, type) values("{0}", "{1}", "5", "2")""".format(a,b))
            a=b
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
while i<24 do
    insert into subscribe_calendar(email, start, end, title, type) values(
    "admin@qq.com", unix_timestamp(now())+3600*24*30+3600*i, unix_timestamp(now())+3600*24*30+3600*(i+1), "", "2");
    set i=i+1;
end while;
delete from subscribe_calendar where SYSDATE()>FROM_UNIXTIME(end);
end;
"""
    with closing(connect_db()) as db:
        db.cursor().execute(sql)
        db.commit()
#show events
#drop event myevent
#show create procedure subscribe
#drop procedure subscribe
#
init_db()
exec_db()
proc()
event()
