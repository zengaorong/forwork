#coding=utf-8
import sys
import MySQLdb
import uuid
from datetime import  datetime

reload(sys)
sys.setdefaultencoding('utf-8')
dataname = "leodb"
host='127.0.0.1'
def updata_watch_todb(nums,error_for):
    conn= MySQLdb.connect(
        host= host,
        port = 3306,
        user='root',
        passwd='7monthdleo',
        db = dataname ,
        charset='utf8'
    )
    cur = conn.cursor()
    sql_str = 'select * from  watcher where id="%s"'%nums

    sql_select = 'select * from  wterror where watcher_id="%s"'%nums
    select_have = cur.execute(sql_select)
    select_list = cur.fetchmany(select_have)
    if select_list:
        return

    names = cur.execute(sql_str)
    info = cur.fetchmany(names)
    if info:
        temp_tuple = info[0]
        dt = datetime.now()
        time = dt.strftime( '%Y-%m-%d %H:%M:%S' )
        # (uuid.uuid1(),temp_tuple[0],time,time,"123456","0","0","0")
        sql_str = '''insert into wterror(id,watcher_id,creat_time,updata_time,work_for,erro_type,log_type,del_type)values("%s","%s","%s","%s","%s","%s","%s","%s")'''%(uuid.uuid1(),temp_tuple[0],time,time,error_for,"0","0","0")
        print sql_str
        names = cur.execute(sql_str)
        print names
    conn.commit()
    conn.close()

def select_wterror():
    conn= MySQLdb.connect(
        host= host,
        port = 3306,
        user='root',
        passwd='7monthdleo',
        db = dataname ,
        charset='utf8'
    )
    cur = conn.cursor()
    sql_str = 'select * from  wterror'
    wterror = cur.execute(sql_str)
    wt_lists = cur.fetchmany(wterror)

    return  wt_lists

def delete_wterror_todb(watcher_id):
    conn= MySQLdb.connect(
        host= host,
        port = 3306,
        user='root',
        passwd='7monthdleo',
        db = dataname ,
        charset='utf8'
    )
    cur = conn.cursor()
    sql_str = 'select * from  wterror where watcher_id="%s"'%watcher_id
    del_data = cur.execute(sql_str)
    del_data_tuple = cur.fetchmany(del_data)
    sql_str = '''insert into wtdel(id,watcher_id,creat_time,updata_time,work_for,erro_type,log_type,del_type)values("%s","%s","%s","%s","%s","%s","%s","%s")'''%(del_data_tuple[0][0],del_data_tuple[0][1],del_data_tuple[0][2],del_data_tuple[0][3],del_data_tuple[0][4],del_data_tuple[0][5],del_data_tuple[0][6],del_data_tuple[0][7])
    cur.execute(sql_str)

    sql_str = 'delete from  wterror where watcher_id="%s"'%watcher_id
    cur.execute(sql_str)

    conn.commit()
    conn.close()
