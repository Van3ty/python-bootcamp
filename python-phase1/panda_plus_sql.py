import pandas as pd
import sqlite3

conn = sqlite3.connect('books.db')

df = pd.read_sql_query("SELECT * FROM books WHERE price > 12", conn)

print(df)