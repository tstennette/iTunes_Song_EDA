#!/usr/bin/python
#this program connects to a mySQL database and inserts rows into the database table Tracks
#I did this to examine my data ahead of my EDA via queries and impute values for skips
import mysql.connector as conn
import csv
import os

hst = input("Enter a server to connect to: ")
usr = input("Enter a user: ")
pswd = input("Enter the password for " + usr + ": ")
db = input("Enter a mySQL database to connect to: ")

mydb = mysql.connector.connect(
  host = hst,
  user = usr,
  passwd = pswd,
  database = db,
  autocommit=True
)
cur = mydb.cursor()

csv_file = input("Enter name of .csv file to upload to " + db)

csv_data = csv.reader(open(csv_file), delimiter = ',')

count = 0
for row in csv_data:
    if count < 1:
        count += 1
        continue
    else:
        print('row: %s', row)
        cur.execute('INSERT INTO Tracks(Title,Time_Length,Artist,Date_Added,Plays,Last_Played,Skips,Last_Skipped) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', row)


db.close()
