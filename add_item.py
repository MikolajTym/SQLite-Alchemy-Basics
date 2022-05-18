import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    insert into scores (id, name, surname, score) values (2, "Jack", "Black", 75)

''')

db.commit()
db.close()
