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

def deal_initial_cards(deck):
	player1.add_cards([deck.deal_one(), deck.deal_one()])
	dealer.add_cards([deck.deal_one(), deck.deal_one()])

def deal_card(deck, player):
	player.add_cards(deck.deal_one())

def show_cards(cards):
	if type(cards) == type([]):
		for item in cards:
			print(item)
	else:
		print(cards)

def display_table(dealer,player1):
	print('=================')
	print(f"{dealer.name}\'s cards:")
	show_cards(dealer.all_cards[0])
	print('=================')
	print(f"{player1.name}\'s cards:")
	show_cards(player1.all_cards)
	print('=================')

# mskin ke dlm player class?
def check_player_value(player):
	value = 0
	ace_count = 0
	for item in player.all_cards:
		value += item.value
		if item.rank == 'Ace':
			ace_count += 1
	if ace_count > 0 and value > 21:
		value = value - (ace_count*10)

	return value

while True:
	round += 1
	print('Round 1')
	deck = Deck()
	deck.shuffle_deck()
	deal_initial_cards(deck)
	player_turn = True
	while player_turn:
		display_table(dealer,player1)
		choice = input('Hit/Stop? (H/S): ')
		if choice in ['H','h']:
			deal_card(deck,player1)
		elif choice in ['S','s']:
			player_turn = False


	a = input('stop')
