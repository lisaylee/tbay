from sqlalchemy import create_engine # Talk to your database using the raw SQL commands
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

engine = create_engine('postgresql://postgres:lawncare@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session() # Session allows you to queue up and execute database transactions
Base = declarative_base() # Acts like a repository for the models

# Items model
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey

class Item(Base):
    __tablename__ = "items"

    # table columns

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)

    # relationships

    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    bids = relationship("Bid", backref="item")

    def __repr__(self):
    	return self.name

# User model
class User(Base):
	__tablename__ = "users"
		
	# table columns
	
	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String, nullable=False)

	# relationships

	items = relationship("Item", backref = "seller")
	
	bids = relationship("Bid", backref="bidder")

	def __repr__(self):
		return self.username

# Bid model
class Bid(Base):
	__tablename__ = "bids"

	# table columns

	id = Column(Integer, primary_key=True) 
	price = Column(Float, nullable = False)

	# relationships	
	item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
	bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)

Base.metadata.create_all(engine)

### CHALLENGE
# Users should be able to auction multiple items (one to many)user, item
# Users should be able to bid on multiple items (one to many)user [bidder], item
# Multiple users should be able to place a bid on an item (one to many), user, bid
