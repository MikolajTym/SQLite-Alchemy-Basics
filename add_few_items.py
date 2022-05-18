from os import name
import sqlite3
import random

try:

    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    print("DB open")

    names = ["Mikel", "Gregory", "James", "Max", "Robert", "Jack", "David"]
    surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis"]
    id = 0

    for _ in range(20):
        name = random.choice(names)
        surname = random.choice(surnames)
        result = random.randint(0,100)

        print(name, surname, result)

        cursor.execute(f'''
        
            insert into scores (id, name, surname, score) values ({id}, "{name}", "{surname}", {result})
        
        ''')

        id+=1

    print("Done")

    db.commit()
    db.close()

except:

    print("Fail")