import pymysql
import logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cur = con.cursor()
sql_del = "DELETE FROM admin_tbl WHERE admin_id = '22'"
logs.logs_on("执行了"+sql_del)
