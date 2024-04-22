import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root',
	)

#create a cursor object
cursorObject = dataBase.cursor()
#create a data base (can do using mysql cli / workbench)
cursorObject.execute("CREATE DATABASE employeedb")

print("all done")