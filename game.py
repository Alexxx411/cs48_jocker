import os
import random
import playerclass

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
same=False
win = False
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

#dealer new
def dealerhit(hand):
	card = deck.pop()
	if card == 11:card = 'J'
	if card == 12:card = 'Q'
	if card == 13:card = 'K'
	if card == 14:card = 'A'
	print "\n"
	print "Dealer draw a new card "+str(card)+" is draw."
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
	global win
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
		win = True
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
		win = False
		play_again()

def score(dealer_hand, player_hand):
	global same
	same = False
	global win

	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		print "Congratulations! You got a Blackjack!\n"
		win = True
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		print "Sorry, you lose. The dealer got a blackjack.\n"
		win = False
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		print "Sorry. You busted. You lose.\n"
		win = False
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)			   
		print "Congratulations. Dealer busts. You win!\n"
		win = True
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
   		print "Sorry. Your score isn't higher than the dealer. You lose.\n"
   		win = False
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)			   
		print "Congratulations. Your score is higher than the dealer. You win\n"
		win = True
	elif total(player_hand) == total(dealer_hand):
		print_results(dealer_hand, player_hand)
		print "Push. Your total is the same as the dealer. You don't lose.\n"	
		same = True

def bet(game_player):
	val = raw_input("How much do you want to bet?\n")
	try:
		betamount = int(val)
		while betamount > game_player.getBalance():
			print "Error: Your bet amount is bigger than your balance! Please try again.\n"
			return bet(game_player)
		while betamount < 0:
			print "Error: your bet amount is smaller than zero! Please try again.\n"
			return bet(game_player)
	except ValueError:
		print "please type a integer!\n"
		bet(game_player)
	return betamount


def check_out(game_player,win,same,betamount): 
	
	if same == True:
		print "push. Now your balance is " + str(game_player.getBalance()) + "."
		return

	elif win == True:
		game_player.winmoney(betamount);
		print "win, Now your balance is " + str(game_player.getBalance()) + "."

		##now we change the data base

		#the second method
		with open("account.txt", "r") as f:
			lines = f.readlines()
		with open("account.txt", "w") as f:
			for line in lines:
				if line.split()[0] != game_player.getName():
					f.write(line)
				else:
					f.write(game_player.getName()+" "+ game_player.getPassword()+ " "+str(game_player.getBalance())+'\n')
		#
		# infile = open('account.txt','r').readlines()
		# with open('account.txt','w') as outfile:
		#     for index,line in enumerate(infile):
		#         if index != game_player.getLine_posi():
		#             outfile.write(line)
		#         # else:
		#         # 	outfile.write(game_player.getName+" "+game_player.getPassword+" "+game_player.winmoney(betamount))
		# print(game_player.getLine_posi() + " modifid!")
		# f=open("account.txt", "a+")
		# f.ge
		# f.write("asd")
		# outfile.close()
		
	elif win == False:
		
		print "Now your balance is " + str(game_player.losemoney(betamount)) + "."
		# print "(lost. Now your balance is " + str(game_player.getBalance()) + "."
		##now we change the data base
		# infile = open('account.txt','r').readlines()
		# with open('account.txt','w') as outfile:
		#     for index,line in enumerate(infile):
		#         if index != game_player.getLine_posi():
		#             outfile.write(line)
		#         # else:
		#         # 	outfile.write(game_player.getName+" "+game_player.getPassword+" "+game_player.winmoney(betamount))
		#         print(game_player.getLine_posi() + " modifid!")
		# outfile.close()
		#the second method
		with open("account.txt", "r") as f:
			lines = f.readlines()
		with open("account.txt", "w") as f:
			for line in lines:
				if line.split()[0] != game_player.getName():
					f.write(line)
				else:
					f.write(game_player.getName()+" "+ game_player.getPassword()+ " "+str(game_player.getBalance())+'\n')
		#
		# f=open("account.txt", "a+")
		# f.write("asd")

def game():
	global win
	choice = 0
	clear()
	num_lines = sum(1 for line in open('account.txt'))
	#how many lines we have in total
	# print(num_lines)

	


	
	win = True
	##need to import the balance and store it to the game_player
	
	count = 0
	
	f = open("account.txt", "r")
	lines = f.readlines()

	# print(lines[num_lines-1])
	info_line = lines[int(lines[num_lines-1])]
	line_posi = lines[num_lines-1]
	# print(line_posi)
	
	# info_line = lines[int(line_posi)]
	
			
	
	game_player = playerclass.player(info_line.split()[0] , info_line.split()[1] ,int(info_line.split()[2]),line_posi)
	print ("WELCOME TO BLACKJACK, " + game_player.getName() + "!\n")
	f.close()
	#clean the last line(which is the line position of the current player)
	infile = open('account.txt','r').readlines()
	with open('account.txt','w') as outfile:
	    for index,line in enumerate(infile):
	        if index != game_player.getLine_posi:
	            outfile.write(line)


	betamount = bet(game_player)
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	print "The dealer is showing a " + str(dealer_hand[0])
	print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
	# blackjack(dealer_hand, player_hand)
	#wtf this line is insane for the bet feature
	quit=False
	while not quit:
		if (total(player_hand)!=21):
			choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
		else:
			choice="s" #here we have the player got a black jack and win 
			win = True
			print "Congratulations! You got a Blackjack!\n"
			check_out(game_player,win,same,betamount)
			play_again()

		if choice == "h":
			hit(player_hand)
			print "You have a " + str(player_hand) + " for a total of " + str(total(player_hand))
			if total(player_hand)>21:
				print('Sorry. You busted. You lose.')
				win = False
				check_out(game_player,win,same,betamount);
				play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				dealerhit(dealer_hand)
				print "Dealer have a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand))
				if total(dealer_hand)>21:
					print('Dealer busts, you win!')
					win = True
					check_out(game_player,win,same,betamount)
					play_again()
			score(dealer_hand, player_hand)
			check_out(game_player,win,same,betamount)
			play_again()
		elif choice == "q":
			print "Bye!"
			quit=True
			exit()
	
if __name__ == "__main__":
	game()




