from tbay import User, Item, Bid, session, engine

# session.query(User).all()

# # # Updating rows
# # user = session.query(User).first()
# # user.username = "solange"
# # session.commit()

# # # Deleting rows (first row)
# # user = session.query(User).first()
# # session.delete(user)
# # session.commit()

def main():

	# add users
	beyonce = User(username = "bknowles", password = "xyz")	
	ariana = User(username = "agrande", password = "abc")
	miley = User(username = "mcyrus", password = "def")
	session.add_all([beyonce, ariana, miley])
	session.commit()

	# Make one user auction a baseball
	baseball = Item(name="baseball", description="Baseball from Babe Ruth's first home run", seller=ariana)
	session.add(baseball)		
	session.commit()
	print("{} started an auction for {} at {}".format(baseball.seller, baseball.name, baseball.start_time.strftime('%m/%d/%y')))


	# Have each other use two bids on the baseball
	starting_bid = Bid(price=100.00, item=baseball, bidder=ariana)
	bknowles_bid = Bid(price=150.00, item=baseball, bidder=beyonce)
	mcyrus_bid = Bid(price=200.00, item=baseball, bidder=miley)
	
	bid_list = [bknowles_bid, mcyrus_bid]
	session.add_all([starting_bid, bknowles_bid, mcyrus_bid])
	session.commit()

	for bid in bid_list:
		print("{} placed a bid on a {} for {}".format(bid.bidder, bid.item, bid.price))

	# Perform a query to find out which user placed the highest bid
	highest_bid = session.query(Bid).order_by(Bid.price.desc()).first()
	print("{} had the highest bid at ${}".format(highest_bid.bidder.username, highest_bid.price))

if __name__ == "__main__":
  	main()


