#Final Project
#Program untuk mengirimkan email kepada beberapa penerima
#Menggunakan smtp GMAIL, sebelumnya email pengirim di setting untuk menerima low security.

# Imports Library smtplib, ssl, csv, getpass

import smtplib,ssl,csv,getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SETUP EMAIL LOGIN 
judul_pesan = input(f"Masukan Subject Email: ")
user_email =input(f"Email Pengirim: ")
user_pass=getpass.getpass(prompt = "Pass email pengirim(Hidden): \n")
try:
    data= open('receiver_list.txt','r')
    read_file = csv.reader(data)
    if data=='':
        print('Data Tujuan Masih Kosong')
    for cetak in read_file:
        #message
        pesan = MIMEMultipart("alternative")
        pesan['Subject']=judul_pesan
        pesan['From']= user_email
        pesan['To']=cetak[1]
        #template
        html = open("template.html")
        template = MIMEText(html.read(),"html") #membaca file sebagai HTML
        pesan.attach(template) #masukan template ke pesan
        #attach file
        filenameCV='dummies.pdf'
        with open(filenameCV,'rb') as lampiran:
            pdf=MIMEBase("application","octet-stream")
            pdf.set_payload(lampiran.read())
            encoders.encode_base64(pdf)
            pesan.attach(pdf)
            pdf.add_header(
                "Content-Disposition",
                "attachment",
                filename=filenameCV
            )
        #send email
        context = ssl.create_default_context()
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(user_email, user_pass)
            server.sendmail(user_email, cetak[1], msg=pesan.as_string())
            server.close()
            print('Email Kepada '+cetak[0]+' Terkirim!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)
            print('Belum Membuat daftar penerima!!\n\n')
    data.close()
except Exception as exception:
    print("Error: %s!\n" % exception) 

#sumber : https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python