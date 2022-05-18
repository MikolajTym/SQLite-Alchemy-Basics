import db
from sqlalchemy.orm import sessionmaker
import random

from datetime import date

# new Session
Session = sessionmaker(bind=db.engine)
session = Session()

# add data
for t in range(10, 20):
    item_id = random.randint(0,1000)
    price = random.randint(20, 50)

    tr = db.transactions(t, str(date.today()), item_id, price) # new object - row in table
    session.add(tr)

session.commit()