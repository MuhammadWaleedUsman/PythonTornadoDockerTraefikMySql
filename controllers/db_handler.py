from .modules import mysql

conn = mysql.connector.connect(
    host="mysql",
    user="user",
    password="pass",
    database="multiuser_db"
)

cursor = conn.cursor()
