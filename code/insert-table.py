import psycopg2
import csv

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")
cur = conn.cursor()

try:
    cur.execute("INSERT INTO daftar_pekerja VALUES (%s, %s, %s, %s, %s)", (1, 'rambo@gmail.com', 'rambo', '613458701', '32103'))
    conn.commit()
    print("insert table sucess")
except:
    print("insert table failed")

try:
    cur.execute("INSERT INTO daftar_pekerja VALUES (%s, %s, %s, %s, %s)", (2, 'simba@hotmail.com', 'simba', '637464947', '16217'))
    conn.commit()
    print("insert table sucess")
except:
    print("insert table failed")

