import mysql.connector
import string

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "#Harsh123",
    database = 'library'
)

cursor = mydb.cursor()
    