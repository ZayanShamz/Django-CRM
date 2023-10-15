import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = '1234',
    )

cmd = db.cursor()

cmd.execute("CREATE DATABASE dcrmdb")
