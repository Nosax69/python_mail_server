import smtplib

sender_mail = input(" Enter a Sender Mail : ")
passwrd = input(" Enter a Sender Mail Password : ")
receiver_mail = input(" Enter a Receiver Mail : ")
 
# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication

s.login(sender_mail, passwrd)
 
# message to be sent

message = "Hello"
 
# sending the mail

s.sendmail(sender_mail, receiver_mail, message)
 
# terminating the session
s.quit()