# lets remake blackjack

import random

cards = [1,1,1,1,
         2,2,2,2,
         3,3,3,3,
         4,4,4,4,
         5,5,5,5,
         6,6,6,6,
         7,7,7,7,
         8,8,8,8,
         9,9,9,9,
         10,10,10,10,
         'J', 'J', 'J', 'J',
         'Q', 'Q', 'Q', 'Q',
         'K', 'K', 'K', 'K']
         
your_cards = []
         
def hit():
    card = cards.pop()
    print("add")
    your_cards.append(card)

total = 0

while total < 16:
    hit()
    
if total > 21:
    print("you lose")
else:
    print("nice")
