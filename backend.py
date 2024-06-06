import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
c=mydb.cursor()
login=False
customer_id=input('Enter Customer ID')
customer_pw=input('Enter Customer PW')
c.execute('select * from customer_detials')
#To retrieve data
for row in c:
    if(customer_id==row[1] and customer_pw==row[2]):
        login=True
        break
if(login):
    print('login successful')
else:
   print('incorrect ID or Password')
#customer_managment

    