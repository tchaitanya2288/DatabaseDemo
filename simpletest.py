import MySQLdb
import sys

# open a database connection
# be sure to change the host IP address, username, password and database name to match your own
conn = MySQLdb.connect(host= "localhost",user="root",passwd="P@ssw0rd",db="mysql")

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute the SQL query using execute() method.
cursor.execute('select * from emp where ESal=90')

# fetch all of the rows from the query
# = cursor.fetchone()

for row in cursor:
    print(row[2])

# print the rows
#for row in data :
 #   print(row[0:7], row[0:3])

# close the cursor object
cursor.close ()

# close the connection
conn.close ()

# exit the program
sys.exit()