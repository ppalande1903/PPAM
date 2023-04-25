import smtplib
from email.mime.text import MIMEText 

body = " welcome to your personal financial dashboard, PPAM  \n This message is to inform you that you have exhausted your monthly spending amount!" 

msg = MIMEText ( body ) 

fromaddr = "priyadarshinicaids121@siesgst.ac.in" 

toaddr = " priyadarshinicaids121@siesgst.ac.in" 

msg [ 'From' ] = fromaddr 

msg [ 'To' ] = toaddr 

msg [ 'Subject' ] = 'Test Mail' 

server = smtplib.SMTP ( 'smtp.gmail.com' , 587 ) 

server.starttls () 

server.login ( " priyadarshinicaids121@siesgst.ac.in" , "piyu2003") 

print ( 'Sending..' ) 

server.send_message ( msg ) 

print ( 'Mail Sent!!' ) 

server. quit ()
