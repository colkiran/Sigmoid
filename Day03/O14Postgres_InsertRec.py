
import psycopg2

conn = psycopg2.connect(database = "sigmoid", user="postgres",
                        host = "localhost",
                        password = "admin",
                        port = 5432)

cur = conn.cursor()

FL = open("InsertRec.txt", "r")

for query in FL.readlines():
    # print(query)
    cur.execute(query)

FL.close()

conn.commit()
cur.close()
conn.close()
