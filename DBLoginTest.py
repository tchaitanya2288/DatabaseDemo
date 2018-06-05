import MySQLdb
class data:
    def __init__(self):
        self.username = input("Enter user name: ")
        self.password= input("Enter Password: ")
a=data()

conn = MySQLdb.connect(host= "localhost",user="root",passwd="P@ssw0rd",db="mysql")

mycursor=conn.cursor()
mycursor.execute("select * from emp where ESal=90")
#usercheck=mycursor.fetchone()

#mycursor2.execute("select * from emp where ESal=90")
#passcheck=mycursor2.fetchone()

for i in mycursor:
    usercheck=i[0]
    passcheck=i[3]

#print(usercheck)
#print(passcheck)
if a.username == usercheck and a.password == passcheck:
    print ("pass")

else:
    print ("sorry")
conn.commit()
conn.close()