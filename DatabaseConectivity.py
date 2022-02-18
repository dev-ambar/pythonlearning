import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="test123", database="mydb")

myCursor = mydb.cursor()
myCursor.execute("select * from product")

result = myCursor.fetchmany(5)
for i in result:
    print(i)
