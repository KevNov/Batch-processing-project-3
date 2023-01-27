import psycopg2
import csv

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")
cur = conn.cursor()

#read csv file table
with open('C:\\Users\\kevnov\\Documents\\Batch processing-project 3\\source\\users_w_postal_code.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

#insert table from csv file
with open('C:\\Users\\kevnov\\Documents\\Batch processing-project 3\\source\\users_w_postal_code.csv','r') as csv_file:
    next(csv_file)
    cur.copy_from(csv_file,'daftar_pekerja',sep=',',columns=('email','name','phone','postal_code'))
conn.commit()       
