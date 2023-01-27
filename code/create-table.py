import psycopg2

#connection to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=576831")
cur = conn.cursor()

#create table
try:
    cur.execute("""
            CREATE TABLE daftar_pekerja(id serial primary key,
            email text, name text, phone text, postal_code text)
        
    """
    )
    conn.commit()
    print("create table sucess")
except:
    print("create table failed")    


