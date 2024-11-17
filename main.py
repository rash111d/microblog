import sqlite3 as sql

connection = sql.connect("main.sl3", 5)
cur = connection.cursor()
cur.execute('DROP TABLE student')
cur.execute("CREATE TABLE IF NOT EXISTS student(id INT, first_name TEXT, last_name TEXT, age INT)")
cur.execute("INSERT INTO student VALUES(1, 'RASHID', 'SHINIBAEV', 10000)")
cur.execute("INSERT INTO student VALUES(1, 'AMIR', 'GUARD', 20000)")
cur.execute("INSERT INTO student VALUES(1, 'ALEX', 'BRO', 45465465)")
cur.execute("INSERT INTO student VALUES(1, 'BATON', 'XLEB', 4125132123)")
cur.execute("INSERT INTO student VALUES(1, 'MOMO', 'MIROV', 626122)")

cur.execute('SELECT * FROM student')
res = cur.fetchall()

print(res)

connection.commit()
connection.close()



