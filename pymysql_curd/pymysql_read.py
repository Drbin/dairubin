import pymysql
import pymysql_curd.logs as logs
con = pymysql.connect(host='localhost', user='root', passwd='root', database='actire_db', charset='utf8')
cursor = con.cursor()
sql_read = "SELECT * FROM admin_tbl"
data = cursor.execute(sql_read)
logs.logs_on("执行了查询操作，SQL语句为：")
logs.logs_on(sql_read)
con.commit()
cursor.close()
con.close()
