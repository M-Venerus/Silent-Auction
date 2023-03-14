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

    new_bid(bid_name, bid_amount)
    another_bid = input("Is there another bidder? Types 'yes' or 'no': ")
    if another_bid == "no":
        auction_running = False

highest_bidder = max(bid_database, key = bid_database.get)
# Format function to force 2 decimal places to represent real dollar value (ex: $25 to $25.00)
highest_bid = "{:.2f}".format(bid_database[highest_bidder])
print(f"The highest bidder is {highest_bidder}, with a bid of ${highest_bid}")

