#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:18:11 2019

@author: chenghui
"""


           

'''codes copied from website
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.XXX.com"  #设置服务器
mail_user="XXXX"    #用户名
mail_pass="XXXXXX"   #口令 
 
 
sender = 'from@runoob.com'
receivers = ['429240967@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP() 
    print ("object created")
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    print
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
    '''
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
print(lines)
for i in range(0, len(namelist)):
    sender = user
    receivers = [emails[i]]
    correct_message = re.sub(r'User',namelist[i],lines)
    message = MIMEText(correct_message, 'plain','utf-8')          
    message['From'] = Header(user,'utf-8') 
    message['To'] = Header(subjects[i],'ascii') # it does not work if you use utf-8 here for information interchange.
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


# for a lot of trial the errors always show that the email address cannot log in. 
# Sometimes if you try to send too many emails through a server, it might lock your account.
#pay attention to the whitepace while writing loops!
#adding 'print'function is a good method when debugging.
      
               
   
    

