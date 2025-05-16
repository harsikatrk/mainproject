
import mysql.connector
cnx=mysql.connector.connect(
    user='root',
    password='Mysql@12345',
    host='127.0.0.1',
    database='billingpayment'
)
 
cur=cnx.cursor(buffered=True)

cur.execute("create table if not exists bills(name varchar(100), phn_no_1 int(10), phn_no_2 int(10), address varchar(100), date_of_order varchar(20), delivery_date varchar(20), delivery_time varchar(20), total_cost_Sweet int(30), total_cost int(30), whole_amount int(50), paid int(20), ch varchar(20), dd_address varchar(50), packaging_details varchar(100), balance int(30), payment_type varchar(10), transaction_id varchar(30));")
def insert_sql( name, phn_no_1, phn_no_2, address, date_of_order, delivery_date, delivery_time, total_cost_Sweet, total_cost, whole_amount, paid, ch, dd_address, packaging_details, balance,payment_type, transaction_id):
    print("insert into bills (name, phn_no_1, phn_no_2, address, date_of_order, delivery_date, delivery_time, total_cost_Sweet, total_cost, whole_amount, paid, ch, dd_address, packaging_details, balance,payment_type, transaction_id) values('" + str(name) + "','" + str(phn_no_1) + "','" + str(phn_no_2) + "','" + str(address) + "', '" + str(date_of_order)+"', '" +str(delivery_date)+"', '"+str(delivery_time) + "', '" + str(total_cost_Sweet)+"', '"+str(total_cost)+"','"+str(whole_amount)+"','"+str(paid)+"','"+str(ch)+"','"+str(dd_address)+"', '"+str(packaging_details)+"', '"+str(balance)+"', '"+str(payment_type)+"', '"+str(transaction_id)+"');")
    cur.execute("insert into bills ( name, phn_no_1, phn_no_2, address, date_of_order, delivery_date, delivery_time, total_cost_Sweet, total_cost, whole_amount, paid, ch, dd_address, packaging_details, balance,payment_type, transaction_id) values('" + str(name) + "','" + str(phn_no_1) + "','" + str(phn_no_2) + "','" + str(address) + "', '" + str(date_of_order)+"', '" +str(delivery_date)+"', '"+str(delivery_time) + "', '" + str(total_cost_Sweet)+"', '"+str(total_cost)+"','"+str(whole_amount)+"','"+str(paid)+"','"+str(ch)+"','"+str(dd_address)+"', '"+str(packaging_details)+"', '"+str(balance)+"', '"+str(payment_type)+"', '"+str(transaction_id)+"');")
    cnx.commit()
'''
cur.execute("Show Tables;")
result = cur.fetchall()
for res in result:
    print(res)
print("\n")

cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00001','HRB','madurai','', '5', '10', '900', 'upi', 'pending', 'pending');")
cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00002','harsika','madurai','take away', '10', '10', '19000', 'cash', 'paid', 'delivered');")
cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00003','krishnan','trichy','door delivery', '2', '1', '400', 'upi', 'pending', 'pending');")
cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00004','xxx','madurai','door delivery', '1', '1', '500', 'upi', 'pending', 'pending');")
cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00005','yyy','madurai','door delivery', '7', '10', '400', 'upi', 'paid', 'pending');")
cur.execute("insert into billing (billnumber, name, address, deliverytype, sweetsKg, savoriesKg, totalamount, paymenttype, paymentstatus, deliverystatus) values('B00006','zzzz','madurai','door delivery', '2', '1', '1500', 'cash', 'pending', 'delivered');")
cnx.commit()
cur.execute("select * from billing;")
result = cur.fetchall()
for res in result:
    print(res)
print("\n")

cur.execute("select * from billing;")
result = cur.fetchone()
for res in result:
    print(res)
print("\n")


cur.execute("Update billing set address='chennai' where name='HRB';")
cnx.commit()
cur.execute("select * from billing;")
result = cur.fetchall()
for res in result:
    print(res)
print("\n")


cur.execute("DELETE from billing where billnumber='B00004';")
cnx.commit()
cur.execute("select * from billing;") # 10 results
result = cur.fetchall() # 10 results
for res in result:
    print(res)


cur.execute("select * from billing;") # 10 results
result = cur.fetchone() # 1 to display; 9 pending
print(result)

    

cur.execute("drop table billing;")
cnx.commit()





'''