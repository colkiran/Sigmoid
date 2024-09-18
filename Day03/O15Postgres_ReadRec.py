import psycopg2
from prettytable import PrettyTable, from_db_cursor

conn = psycopg2.connect(database = "sigmoid", user="postgres",
                        host = "localhost",
                        password = "admin",
                        port = 5432)

cur = conn.cursor()

query = "select * from players"

cur.execute(query)

prtyTbl = from_db_cursor(cur)

cur.close()
conn.close()

print(prtyTbl)
