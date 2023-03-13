### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


  def check_for_ace(self, card):
    if card.value == 1: # "=" was missing
      return True
    else:               # ":" was missing
      return False
   
# "dif" should be "def" (line 20)
# a "," is missing after "card1" (line 20)
# the code should have a correct indent from "if" statement to the last "return" // after the first "return", "card" should be card1 (line 22)

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
  
# a value is given to "total": '= 0'
#space added in the string after "of"
#added str()
#indetation correction

  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)