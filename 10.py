import mysql.connector

cnx = mysql.connector.connection.MySQLConnection(
    user='root',
    password='Mysql@12345',
    host='127.0.0.1',
    database='emp'
)