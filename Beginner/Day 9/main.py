# from replit import clear
import art

print(art.logo)

bidders = []
end = False

def add_bidders(name, bid):
  bidders.append({
    "name": name,
    "bid": bid
  })

while not end:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))

  add_bidders(name, bid)

  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

  if more_bidders == 'no':
    end = True
#   else:
#     clear()


winner = bidders[0]
for bidder in bidders:
  if(bidder["bid"] > winner["bid"]):
    winner = bidder

print(f"The winner is: {winner['name']}")
  
