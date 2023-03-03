import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db_live",
    user="postgres",
    password="password"
)

cursor = conn.cursor()

cursor.execute("SELECT * from test;")
data = cursor.fetchall()
print(data)
conn.close()