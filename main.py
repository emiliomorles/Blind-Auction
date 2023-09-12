import os #it helps cleaning the previous stage
from art import logo
print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finish = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela":123, "James":321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")

while not bidding_finish:
  name = input("What is your name?: ")
  amount = int(input("What's your bid?: $"))
  bids[name] = amount
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_continue == "no":
    bidding_finish = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    os.system('cls' if os.name == 'nt' else 'clear') #with this code the game would clean the previous stage
