import os
import random


class Blackjack:

	deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	def __init__(self):
		self.betamount=0;
		self.totalgame=0;
		self.gamewin=0;

	def showinformation(self):
		print "Bet amount : ", self.betamount, "\n"
		print "Total number of games you play : ", self.totalgame, "\n"
		print "The number of games you win : ", self.gamewin, "\n"

	def bet():
		betamount = raw_input("How much do you want to bet? :")

	def deal(deck):
		hand = []
		for i in range(2):
			random.shuffle(deck)
			card = deck.pop()
			if card == 11:card = "J"
			if card == 12:card = "Q"
			if card == 13:card = "K"
			if card == 14:card = "A"
			hand.append(card)
			return hand

	def play_again():
		again = raw_input("Do you want to play again? (Y/N) : ").lower()
		if again == "y":
			bet()
			dealer_hand = []
			player_hand = []
			deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
			game()
		else:
			print "Bye!"
			exit()

	def total(hand):
		total = 0
		for card in hand:
			if card == "J" or card == "Q" or card == "K":
				total+= 10
			elif card == "A":
				if total >= 11: total+= 1
				else: 
					total+= 11
			else:
				total += card
		return total

	def hit(hand):
		card = deck.pop()
		if card == 11:card = 'J'
		if card == 12:card = 'Q'
		if card == 13:card = 'K'
		if card == 14:card = 'A'
		print "\n"
		print "a new card "+str(card)+" is draw."
		hand.append(card)
		return hand

	def clear():
		if os.name == 'nt':
			os.system('CLS')
		if os.name == 'posix':
			os.system('clear')

	def print_results(dealer_hand, player_hand):
		print "\n"
		print "The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))

	def blackjack(dealer_hand, player_hand):
		if total(player_hand) == 21:
			print_results(dealer_hand, player_hand)
			print "Congratulations! You got a Blackjack!\n"
			play_again()
		elif total(dealer_hand) == 21:
			print_results(dealer_hand, player_hand)		
			print "Sorry, you lose. The dealer got a blackjack.\n"
			play_again()

	def score(dealer_hand, player_hand):
		if total(player_hand) == 21:
			print_results(dealer_hand, player_hand)
			print "Congratulations! You got a Blackjack!\n"
		elif total(dealer_hand) == 21:
			print_results(dealer_hand, player_hand)		
			print "Sorry, you lose. The dealer got a blackjack.\n"
		elif total(player_hand) > 21:
			print_results(dealer_hand, player_hand)
			print "Sorry. You busted. You lose.\n"
		elif total(dealer_hand) > 21:
			print_results(dealer_hand, player_hand)			   
			print "Congratulations. Dealer busts. You win!\n"
		elif total(player_hand) < total(dealer_hand):
			print_results(dealer_hand, player_hand)
   			print "Sorry. Your score isn't higher than the dealer. You lose.\n"
		elif total(player_hand) > total(dealer_hand):
			print_results(dealer_hand, player_hand)			   
			print "Congratulations. Your score is higher than the dealer. You win\n"
		elif total(player_hand) == total(dealer_hand):
			print_results(dealer_hand, player_hand)
			print "Push. Your total is the same as the dealer. You don't lose.\n"	

	def game():
		choice = 0
		clear()
		print "WELCOME TO BLACKJACK!\n"
		bet()
		dealer_hand = deal(deck)
		player_hand = deal(deck)
		print "The dealer is showing a " + str(dealer_hand[0])
		print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
		blackjack(dealer_hand, player_hand)
		quit=False;
		while not quit:
			if (total(player_hand)!=21):
				choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
			else:
				choice="s"
			if choice == "h":
				hit(player_hand)
				print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
				if total(player_hand)>21:
					print('Sorry. You busted. You lose.')
					play_again()
			elif choice == "s":
				while total(dealer_hand) < 17:
					hit(dealer_hand)
					print "Dealer have a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
					if total(dealer_hand)>21:
						print('Dealer busts, you win!')
						play_again()
				score(dealer_hand, player_hand)
				play_again()
			elif choice == "q":
				print "Bye!"
				quit=True;
				exit()

if __name__ == "__main__":
	game()

