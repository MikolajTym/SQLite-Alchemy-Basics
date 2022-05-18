import requests # czytanie danych z API REST
import time
import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

def add_price(coin, currency, price):
    p = db.Prices(coin, currency, price) # Konsturktor dla bazy danych

    session.add(p) # dodanie rekordu
    session.commit() # zapisanie zmian

while True:
    res = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()
    print(res["data"]["base"], res["data"]["currency"], res["data"]["amount"])
    add_price(res["data"]["base"], res["data"]["currency"], res["data"]["amount"])

    time.sleep(10) # czekanie 10 sekund

session.close()