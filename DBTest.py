
import MySQLdb
conn = MySQLdb.connect(host= "localhost",user="root",passwd="P@ssw0rd",db="mysql")
x = conn.cursor()

try:
   x.execute("""INSERT INTO dept VALUES ('praveen1',1000)""")
   #sql="""create table dept(deptname CHAR, deptno INT)"""
   #sql="""insert into dept VALUES('IT',1231)"""
   #x.execute("""INSERT INTO DEPT VALUES('IT',1231)""")
   conn.commit()
except:
   conn.rollback()

conn.close()