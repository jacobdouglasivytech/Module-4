
import csv
with open('books.csv') as book:
    cin = csv.DictReader(book)
    books = [row for row in cin]
    
print(books) 

import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
conn.execute('''CREATE TABLE book (title TEXT, author TEXT, year INT)''')

