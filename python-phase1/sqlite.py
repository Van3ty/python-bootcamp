import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books(
               id INTEGER,
               title TEXT,
               price REAL
               )""")




conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
print(rows)


