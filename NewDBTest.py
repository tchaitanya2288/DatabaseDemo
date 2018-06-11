import MySQLdb as db

HOST="localhost"
USER="root"
Password="P@ssw0rd"
DB="mysql"

try:
    connection=db.connect(host=HOST, user=USER, password=Password, db=DB)
    dbhandler=connection.cursor()
    dbhandler.execute("select * from emp")
    result=dbhandler.fetchall()
    for item in result:
        print(item[0])

except Exception as e:
    print(e)
connection.close()



