#!C:\Python312\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")

form=cgi.FieldStorage()
fname=form.getvalue("name")
fage=form.getvalue("age")
fcity=form.getvalue("city")
fcontact=form.getvalue("contact")

print(fname,fage,fcity,fcontact)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="harvard"
)

mycursor=mydb.cursor()

sql="INSERT INTO user(Name,Age,City,Contact)VALUES(%s,%s,%s,%s)"
val=(fname,fage,fcity,fcontact)

mycursor.execute(sql,val)
mydb.commit()