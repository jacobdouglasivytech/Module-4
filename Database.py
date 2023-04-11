import csv
with open('books.csv') as book:
    cin = csv.DictReader(book)
    books = [row for row in cin]
    
print(books) 

import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
conn.execute('''drop table book''')
conn.execute('''CREATE TABLE IF NOT EXISTS book (title TEXT, author TEXT, year INT)''')
ins = 'INSERT INTO book (title, author, year) VALUES (?, ?, ?)'
curs.execute(ins, ('The Weirdstone of Brisingamen', 'Alan Garner', 1960))
curs.execute(ins, ('Perdido Street Station', 'China Miéville', 2000))
curs.execute(ins, ('Thus!', 'Terry Pratchett', 2005))
curs.execute(ins, ('The Spellman Files', 'Lisa Lutz', 2007))
curs.execute(ins, ('Small Gods', 'Terry Pratchett', 1992))
conn.commit()
curs.execute('SELECT title FROM book ORDER BY title')
rows = curs.fetchall()
print(rows)
curs.execute('SELECT * FROM book ORDER BY year')
rows = curs.fetchall()
print(rows)
curs.close()
conn.close()
 
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///books.db', echo=True)
conn = engine.connect()
result = conn.execute(text('SELECT title FROM book ORDER BY title')).all()
for row in result:
    print(row)
conn.close()


