import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books(
               id INTEGER,
               title TEXT,
               price REAL
               )""")



cursor.execute("""
               INSERT INTO books VALUES(1, 'Gatsby', 15.99)
               """)

cursor.execute("""
               INSERT INTO books VALUES(2, '1984', 10.99)
               """)

cursor.execute("""
               INSERT INTO books VALUES(3, 'To Kill a Mockingbird', 12.99)
               """)

cursor.execute("""
               INSERT INTO books VALUES(4, 'Pride and Prejudice', 9.99)
               """)

cursor.execute("""
               INSERT INTO books VALUES(5, 'The Catcher in the Rye', 14.99)
               """)

cursor.execute("""
               INSERT INTO books VALUES(6, 'The Hobbit', 11.99)
               """)

conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()
print(rows)

