'''
Game
'''

from player import Player
from deck import Deck

# initialization
print('Welcome to Black Jack 21!')
player_name = input('Enter name: ')
player1 = Player(player_name)
dealer = Player('Dealer')
round = 0

def dealing_cards(deck):
	player1.add_cards([deck.deal_one(), deck.deal_one()])
	dealer.add_cards([deck.deal_one(), deck.deal_one()])

while True:
	round += 1
	print('Round 1')
	deck = Deck()
	deck.shuffle_deck()
	dealing_cards(deck)
	print(player1)
	print(dealer)
	a = input('stop')
