import sqlite3

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    select * from scores

''')

rows = cursor.fetchall()
for r in rows:
    print(r[1], r[2], r[3])


cursor.execute('''

    select count(*) from scores

''')

rows = cursor.fetchone()
print("Rows", rows[0])

db.commit()
db.close()