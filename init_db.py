import sqlite3

connection = sqlite3.connect('database.db')



cur = connection.cursor()

a = cur.execute("SELECT usr FROM user WHERE id = '1'").fetchmany()




connection.commit()
print(a)
connection.close()