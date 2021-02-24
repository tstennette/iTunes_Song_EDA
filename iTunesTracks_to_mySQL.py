#!/usr/bin/python
import mysql.connector as conn
import csv
import os

db = conn.connect(host="localhost",   
                     user="tyler",         
                     passwd="terry8330!",  
                     db="iTunesMusic",
                     autocommit = True)        

cur = db.cursor()

csv_data = csv.reader(open('Track_List_YYYY_MM_DD.csv'), delimiter = ',')

count = 0
for row in csv_data:
    if count < 1:
        count += 1
        continue
    else:
        print('row: %s', row)
        cur.execute('INSERT INTO Tracks(Title,Time_Length,Artist,Date_Added,Plays,Last_Played,Skips,Last_Skipped) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', row)


db.close()
