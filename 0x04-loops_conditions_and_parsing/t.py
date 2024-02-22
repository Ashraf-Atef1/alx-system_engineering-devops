import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "123"
)


cursor = mydb.cursor()


cursor.execute("CREATE DATABASE geeksforgeeks")