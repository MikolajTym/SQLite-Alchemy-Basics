from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# connect with db
engine = create_engine('sqlite:///db.sqlite')
base = declarative_base()

class Prices(base):
    __tablename__ = "prices"

    coin = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    currency = Column(String, primary_key=True)
    price = Column(Integer)

    def __init__(self, coin, currency, price):

        self.coin = coin
        self.currency = currency
        self.price = price
        self.date = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")

base.metadata.create_all(engine)