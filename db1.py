import mysql.connector
cnx = mysql.connector.connect(
    user='root',
    password='Mysql@12345',
    host='127.0.0.1',
    database='employees'
)

# cnx.connect()
# cnx.close()

cur = cnx.cursor()

cur.execute("create table emp (name Varchar(255), mobile bigint);")

cur.execute("Show Tables;")
result = cur.fetchall()
for res in result:
    print(res)

cur.execute("insert into emp (name, mobile) values('HRB',8825410600);")
cnx.commit()

cur.execute("select * from emp;")
result = cur.fetchall()
for res in result:
    print(res)

cur.execute("Update emp set mobile=8825410600 where name='HRB';")
cnx.commit()

