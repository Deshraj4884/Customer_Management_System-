import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title('Customer Management System')
st.sidebar.image('https://assets-global.website-files.com/59e16042ec229e00016d3a66/60b8f057616cb823051a2fda_blog-listing%20(11).gif')
choise=st.sidebar.selectbox('Menu',('Home','Admin','Customer'))
if(choise=='Home'):
    st.image('https://praveenekanthamedia.com/images/keyTopic/manage.gif')     
    st.header('Hey! Welcome')                                                  
    st.write('Here We alway for you')
elif(choise=='Admin'):
    if 'Login' not in st.session_state:
        st.session_state['Login']=False
    id=st.text_input('Enter the ID')                        
    pw=st.text_input('Enter the Password')
    btn=st.button('Login')
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
        c=mydb.cursor()
        c.execute('select * from admins')
        for row in c:
            if(row[0]==id and row[1]==pw):
                st.session_state['Login']=True 
                break
        if(st.session_state['Login']==False):
            st.subheader('Incorrect ID or Password')
    if(st.session_state['Login']==True):
        st.subheader('Login Successful')  
        choise2=st.selectbox('Features',('None','View All Customers','Update Customer Details','Add New Customer','Remove Customer','View Customer Comments'))
        if(choise2=='View All Customers'):                                                     
            mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
            c=mydb.cursor()
            c.execute('select * from customer_detials')
            l=[]
            for r in c:
                l.append(r)
            df=pd.DataFrame(data=l,columns=['Date_of_join','customer_id','customer_pw','costumer_name','age','gender','email','address','Comment_via_Admin'])
            st.dataframe(df)
        elif(choise2=='Add New Customer'):
            customer_id=st.text_input('Enter Customer ID')
            customer_pw=st.text_input('Enter Customer PW')
            costumer_name=st.text_input('Enter Customer Name')
            age=st.text_input('Age')
            gender=st.text_input('Gender')
            email=st.text_input('Enter the Email')
            address=st.text_input('Enter the Address')
            Comments=st.text_input('Any Comments')
            btn2=st.button('Add New Customer')                                                                                                                 
            if(btn2):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('insert into customer_detials values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(doi,customer_id,customer_pw,costumer_name,age,gender,email,address,Comments))
                mydb.commit()
                st.header('New Customer Added Successfuly')
        elif(choise2=='Update Customer Details'):
                choise3=st.selectbox('Features',('None','Customer Password','Costumer Name','Age','Gender','Email','Address','Comment'))
                if(choise3=='Customer Password'):
                    customerID=st.text_input('Enter Customer ID')
                    customerPW=st.text_input('Enter New Password')
                    btn3=st.button('Update the Customer detials')
                    if(btn3):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set customer_pw=%s where customer_id=%s',(customerPW,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')
                elif(choise3=='Costumer Name'):
                    customerID=st.text_input('Enter Customer ID')
                    Costumer_Name=st.text_input('Enter New Name')
                    btn4=st.button('Update the Customer detials')
                    if(btn4):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set costumer_name=%s where customer_id=%s',(Costumer_Name,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')    
                elif(choise3=='Age'):
                    customerID=st.text_input('Enter Customer ID')
                    Age=st.text_input('Age')
                    btn5=st.button('Update the Customer detials')
                    if(btn5):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set age=%s where customer_id=%s',(Age,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')    
                elif(choise3=='Gender'):
                    customerID=st.text_input('Enter Customer ID')
                    Gender=st.text_input('Gender')
                    btn6=st.button('Update the Customer detials')
                    if(btn6):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set gender=%s where customer_id=%s',(Gender,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')  
                elif(choise3=='Email'):
                    customerID=st.text_input('Enter Customer ID')
                    Email=st.text_input('Enter New Email')
                    btn7=st.button('Update the Customer detials')
                    if(btn7):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set email=%s where customer_id=%s',(Email,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')  
                elif(choise3=='Address'):
                    customerID=st.text_input('Enter Customer ID')
                    Address=st.text_input('Enter New Address')
                    btn8=st.button('Update the Customer detials')
                    if(btn8):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set address=%s where customer_id=%s',(Address,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')

                elif(choise3=='Comment'):
                    customerID=st.text_input('Enter Customer ID')
                    Comment=st.text_input('Enter Comment')
                    btn10=st.button('Update the Customer detials')
                    if(btn10):
                        doi=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                        c=mydb.cursor()
                        c.execute('update customer_detials set Comment_via_Admin=%s where customer_id=%s',(Comment,customerID))
                        mydb.commit()
                        st.header('Customer detials Updated Successfuly')                                          
        elif(choise2=='Remove Customer'):
            customerid=st.text_input('Enter Customer ID')
            btn9=st.button('Delete')
            if(btn9):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('delete from customer_detials where customer_id=(%s)',[(customerid)])
                mydb.commit()
                st.header('Customer Deleted Successfuly')

        elif(choise2=='View Customer Comments'):
            CUSTOMER_ID=st.text_input('Enter CUSTOMER ID')
            btn11=st.button('View')
            if(btn11):
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('select * from Comments where customer_id=%s',[CUSTOMER_ID])
                l=[]
                for r in c: 
                    l.append(r)
                df=pd.DataFrame(data=l,columns=['customer_id','comments'])
                st.dataframe(df)


elif(choise=='Customer'):
    if 'login2' not in st.session_state:
        st.session_state['login2']=False
    id=st.text_input('Enter Customer ID')
    password=st.text_input('Enter Password')
    btn=st.button('login')
    if btn:
        mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
        c=mydb.cursor()
        c.execute('select * from customer_detials')
        for row in c:
            if(row[1]==id and row[2]==password):
                st.session_state['login2']=True
                break
        if(st.session_state['login2']==False):
            st.subheader('Incorrect ID or Password')
    if(st.session_state['login2']==True):
        st.subheader('Login Successful')
        choise2=st.selectbox('Features',('None','View Customer Details','Add Comments','View Comments'))
        if(choise2=='View Customer Details'):
            CUSTOMER_ID=st.text_input('Enter CUSTOMER ID')
            btn2=st.button('View Details')
            if(btn2):
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('select * from customer_detials where customer_id=%s',[CUSTOMER_ID])
                l=[]
                for r in c: 
                    l.append(r)
                df=pd.DataFrame(data=l,columns=['Date_of_join','customer_id','customer_pw','costumer_name','age','gender','email','address','Comment_via_Admin'])
                st.dataframe(df)
        elif(choise2=='Add Comments'):
            Customer_ID=st.text_input('Customer ID')
            Comment=st.text_input('Enter Comment')
            btn3=st.button('Add Comment')
            if(btn3):
                doi=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('update Comments set comments=%s where customer_id=%s',(Comment,Customer_ID))
                mydb.commit()
                st.header('Comment Updated Successfuly') 

        elif(choise2=='View Comments'):
            CUSTOMER_ID=st.text_input('Enter CUSTOMER ID')
            btn4=st.button('View')
            if(btn4):
                mydb=mysql.connector.connect(host='localhost',user='root',password='****',database='customer_managment')
                c=mydb.cursor()
                c.execute('select * from Comments where customer_id=%s',[CUSTOMER_ID])
                l=[]
                for r in c: 
                    l.append(r)
                df=pd.DataFrame(data=l,columns=['customer_id','comments'])
                st.dataframe(df)




