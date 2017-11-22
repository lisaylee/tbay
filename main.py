from tbay import User, Item, Bid 

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

	# Make one user auction a baseball
	baseball = Item(name="baseball", description="Baseball from Babe Ruth's first home run", seller=ariana)
	session.add(baseball)
	session.commit()
	print("{} started an auction for {} at {}".format(baseball.owner.username, baseball.name, baseball.start_time))


	# Have each other use two bids on the baseball
	bknowles_bid = bid(price=150.00, item=baseball, user=bknowles)
	mcyrus_bid = bid(price=200.00, item=baseball, user=mcyrus)
	
	session.add_all([beyonce, ariana, miley, bknowles_bid, mcyrus_bid])
	session.commit()

	# Perform a query to find out which user placed the highest bid
	highest_bid = session.query(bid).order_by(desc(bid.price))
	print("{} had the highest bid at ${}".format(highest_bid.bidder.username, highest_bid.price))

	if __name__ == "__main__":
  		main()
