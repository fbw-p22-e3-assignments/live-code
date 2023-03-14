from psycopg2.pool import SimpleConnectionPool

pool = SimpleConnectionPool(minconn=1, maxconn=2, 
                            host="localhost",
                            database="python_db",
                            user="postgres",
                            password="password")

SQL_active = "select datname from pg_stat_activity"
SQL_insert = "insert into test(num, data) values(123, 'HELLO CONNECTIONS again')"
SQL_xmin = 'select xmin, txid_current(), * from test'

conn1 = pool.getconn()
conn2 = pool.getconn()
pool.putconn(conn1)
conn3 = pool.getconn()
# curs1 = conn1.cursor()
# curs1_2 = conn1.cursor()
# curs2 = conn2.cursor()
# curs1.execute(SQL_insert)
# curs1_2.execute(SQL_insert)
# conn1.commit()
# conn2.commit()
# curs1.execute(SQL_xmin)
# print(curs1.fetchall())
