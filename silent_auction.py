# Silent Auction

import assets
print(assets.hammer)
print("Welcome to the Silent Auction Bid Recorder.")

bid_database = {}

def new_bid(name, amount):
    bid_database[name] = amount

auction_running = True
while auction_running:
    bid_name = input("Name of bidder: ")
    bid_amount = float(input("Bid amount: $"))
    # Format bid_amount to 2 decimal places regardless of decimals. Real represenetation of dollar (ex: $25.00)
    bid_amount = "{:.2f}".format(bid_amount)

    new_bid(bid_name, bid_amount)
    another_bid = input("Is there another bidder? Types 'yes' or 'no': ")
    if another_bid == "no":
        auction_running = False

highest_bidder = max(bid_database, key = lambda key: bid_database[key])
print(bid_database)
print(f"The highest bidder is {highest_bidder}, with a bid of ${bid_database[highest_bidder]}")

