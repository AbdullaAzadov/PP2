import psycopg2
 
conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345", host="127.0.0.1")
print("Подключение установлено")
conn.close()