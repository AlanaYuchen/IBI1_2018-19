#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:18:11 2019

@author: Alana
"""

#-------------------Determine whether the email address is legal---------------
# creat some empty list to store seperated information
email_address=[]
namelist = []
subjects = []
emails = []
#seperate information to different lists
import re
email = open('address_information.csv', 'r') 
#split the csv file by comma
for line in email:
    lines = re.split(r',', str(line))
    if re.search (r'@', lines[1])==None: #check whether the information in line[1] is an email address
        continue #skip the following codes and go to the next for loop directly if the line is not an email address
    email_address = lines[1]
    p = re.compile(r"[^@]+@[^@]+\.[^@]+") #matching the correct format of an emial address
    if not p.match(email_address): 
           print (email_address,': Wrong Address!') 
    else:
           print (email_address,': Correct Address!') 
           namelist += [lines[0]]
           subjects += [lines[2]]
           emails +=[lines[1]]
           
#-------------------------sending the email---------------------------------           
import smtplib
from email.mime.text import MIMEText
from email.header import Header
user= input('user email address:')
password = input('password:')
host = 'smtp.'+ re.findall ('@(.+)',user)[0]
mail_host= host
mail_user= user
mail_pass=password
text = open('body.txt','r')
lines =''
for line in text:
    lines = lines + line
for i in range(0, len(namelist)):
    sender = user
    receivers = [emails[i]]
    correct_message = re.sub(r'User',namelist[i],lines)
    message = MIMEText(correct_message, 'plain','utf-8')          
    message['From'] = Header(user,'utf-8') 
    message['To'] = Header(subjects[i],'ascii') # it went wrong if using 'utf-8' here for information interchange.
    subject = subjects[i]                       #askii: American Standard Code for Information Interchange
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)  #connect to the server  
        smtpObj.login(mail_user,mail_pass) #login email acount  
        smtpObj.sendmail(sender, receivers, message.as_string()) 
        print ('Mail sent successfully')
    except smtplib.SMTPException:
        print ('Mail did not send successfully')
        
email.close()
text.close()

# for a lot of trial the errors always show that the email address cannot log in. 
# Sometimes after trying to send too many emails through a server, the account might be locked.
#pay attention to the whitepace while writing loops!
#adding 'print'function is a good method when debugging.
      
               
   
    

