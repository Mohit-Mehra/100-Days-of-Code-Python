import os

# Clearing the Screen os.system("cls")

from art import logo

print(logo)

bids = {}
biddind_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}.")


while not biddind_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? ₹"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if should_continue == "no":
        biddind_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        os.system("cls")
