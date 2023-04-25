import streamlit as st
import smtplib as s
import os

def main():
    st.title("email sender web application")
    st.write("build with streamlit and python")
    activities=["send email","about"]
    choice=st.sidebar.selectbox("select activities",activities) 
    if choice=="send email:":
      
        email_sender=st.text_input("enter user email")
        password=st.text_input("enter your password-",type="password")
        email_reciever=st.text_input("enter reciever mail:")
        subject=st.text_input("your email suject")
        body=st.text_area("your email")
        if st.button("send email"):
            try:
                connection=s.SMTP('smtp.gmail.com,587')
                connection.starttls()
                connection.login(email_sender,password)
                message="subject:{}\n\n{}".format(subject,body)
                connection.sendmail(email_sender,email_reciever,message)
                connection.quit()
                st.success("emsil sent successfully")
               
            except Exception as e:
                if email_sender=="":
                    st.error("please fill user email field")
                   
                elif password=="":
                    st.error("please fill password")
                  
                elif email_reciever=="":
                    st.errror("please fill reciever mail")
                 
                else:
                    a=os.system("ping www.google.com")
                    if a==1:
                        st.error("please connect to internet")
                   
                    else:
                        st.error("wrong email or password")
                    
    else:
        st.markdown('THIS APP IS DEVELOPED BY SE AIDS')                            




 
                

