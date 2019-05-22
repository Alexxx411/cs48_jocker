from time import sleep
from random import randint

s1 = 1
s2 = 2
s3 = 3
s6 = 6
s10 = 10

def main():
    selected = None
    while selected != 0:
        print_menu()
        selected = input()
        if selected:
            selected = test_menu_selected(selected)
        else:
            print("Please enter an option.")


def print_menu():
        print("""\n{0}Menu{0}
0.) Quit
1.) Play Blackjack
Please enter an option from above""".format(("-" * 15)))


def check_int(x):
    for char in x:
        if char in "0123456789":
            result = True
        else:
            result = False
            break
    return result


def test_menu_selected(x):
    is_int = check_int(x)
    if is_int:
        x = int(x)
    else:
        print("Please only enter an integer")
        return x
    if x == 0:
        return x
    if x == 1:
        explain_blackjack()
    if x == 2:
        global s1
        global s2
        global s3
        global s6
        global s10
        s1 = s2 = s3 = s6 = s10 = 0
        explain_blackjack()
    else:
        print("Please only enter one of the available options.")
        return x


def test_player_options(option):
    is_int = check_int(option)
    if is_int:
        option = int(option)
    else:
        print("Please only enter one of the available choices")
        return False
    if option == 1:
        return "hit"
    elif option == 2:
        return "stay"
    else:
        print("Please only enter one of the available choices")
        return False


def explain_blackjack():
    global needs_explain
    if needs_explain:
        needs_explain = False
        print("Thanks for playing blackjack. The rules are as follows:")
        sleep(s3)
        print("""1.) The dealer will deal you and himself two cards each.
    You will be able to see BOTH of your cards and ONE of the dealer's cards.""")
        sleep(s6)
        print("""2.) The object is to get as close to 21 points as possible without going over.
    The dealer will try to get as close to 21 as possible as well.
    He has to keep drawing until his points are higher than 17.
    You may stop drawing whenever you like""")
        sleep(s10)
        print("""3.) All number cards (2-10) are worth their number value in points
    All face cards(Jack, Queen, King) are worth 10 points
    The Ace is worth either 1 or 11, it is up to you to decide.""")
        sleep(s10)
        print("Press enter when you are ready to play")
        input()
        play_blackjack()
    else:
        play_blackjack()


def play_blackjack():
    deck = load_deck()
    deck = shuffle_deck(deck)
    players_hand = []
    dealers_hand = []
    for i in range(2):
        deal_card(deck, "player", players_hand)
        deal_card(deck, "dealer", dealers_hand)
    play_round(players_hand, dealers_hand, deck)


def load_deck():
    deck = [0] * 52
    suits = ["hearts", "diamonds", "spades", "clubs"]
    ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    i = s_i = r_i = 0
    c_i = 1
    for card in deck:
        rank = ranks[r_i]
        suit = suits[s_i]
        new_card = "{} of {}".format(rank, suit)
        deck[i] = [c_i, new_card]
        if r_i < 12:
            r_i += 1
            c_i += 1
        else:
            r_i = 0
            c_i = 1
            s_i += 1
        i += 1
    return deck


def shuffle_deck(old_deck):
    new_deck = []
    used_indexes = []
    while len(new_deck) < 52:
        index_to_use = randint(0, 51)
        if index_to_use in used_indexes:
            continue
        else:
            new_deck.append(old_deck[index_to_use])
            used_indexes.append(index_to_use)
    return new_deck


def deal_card(deck, user, hand):
    the_card = deck[0]
    if user == "player":
        hand.append(the_card)
    elif user == "dealer":
        hand.append(the_card)
    deck.remove(the_card)


def play_round(p_hand, d_hand, deck):
    print("The dealer has been dealt a(n) {} and an unknown card.".format(d_hand[0][1].upper()))
    sleep(s3)
    print("You have been dealt a(n) {} and a(n) {}".format(p_hand[0][1].upper(), p_hand[1][1].upper()))
    sleep(s3)
    print("What would you like to do?\n")
    sleep(s2)
    print("""1.) Hit (get another card)
2.) Stay (stop playing and keep the cards you have now)\n""")
    no_choice = True
    while no_choice:
        selected = input().lower()
        if selected:
            choice = test_player_options(selected)
            if not choice:
                continue
            else:
                no_choice = False
                if choice == "hit":
                    p_hand, deck = hit(p_hand, deck)
                    no_choice = True
                elif choice == "stay":
                    stay(p_hand, d_hand, deck)
        else:
            print("Please enter a valid option")


def determine_player_points(hand):
    value = 0
    for card in hand:
        # if card has 3 entries, it is an ace with a special value
        if len(card) == 3:
            value += card[2]
        # else if its value is 11 or above, it is a face card
        elif card[0] < 11:
            value += card[0]
        # else, its value is its points
        else:
            value += 10
    if value == 21:
        print(value)
        print("You win! Want to play again?")
        main()
    elif value > 21:
        print(value)
        print("You've busted! Dealer wins, want to play again?")
        main()
    else:
        return False, value


def hit(hand, deck):
    value = 0
    for card in hand:
        if card[0] < 11:
            value += card[0]
        else:
            value += 10
    if value < 21:
        card = deck[0]
        hand.append(card)
        if card[0] < 11:
            value += card[0]
        else:
            value += 10
        print("You were dealt a {}, here is your new hand:".format(card[1].upper()))
        sleep(s2)
        new_hand = []
        for card in hand:
            name = card[1].upper()
            new_hand.append(name)
        print(", ".join(new_hand))
        sleep(s2)
    if value > 21:
        print("That is {} points, you've busted! Dealer wins, want to play again?".format(value))
        sleep(s2)
        main()
    else:
        print("What would you like to do?")
        print("""1.) Hit Again
2.) Stay""")
        deck.remove(card)
        return hand, deck


def hit_dealer(hand, deck):
    # determine if dealer has more than 17 points
    #   if he does see if he has over 21, if so, end game
    #   else, compare points
    # else, deal him a card and see if he has 17 points now
    d_points = 0
    first_time = True
    while d_points < 17:
        d_points = 0
        aces = []
        for card in hand:
            if card[0] == 1:
                aces.append(card)
                continue
            elif 11 > card[0] > 1:
                d_points += card[0]
            elif card[0] >= 11:
                d_points += 10
        for card in aces:
            option1 = d_points + 11
            option2 = d_points + 1
            difference1 = 21 - option1
            difference2 = 21 - option2
            if difference1 < 0 or (option1 == 21 and len(aces) > (aces.index(card) + 1)):
                d_points += 1
            elif difference1 < difference2:
                d_points += 11
        if d_points >= 17:
            print("The dealer has:")
            sleep(s1)
            new_hand = []
            for card in hand:
                name = card[1].upper()
                new_hand.append(name)
            print(", ".join(new_hand))
            sleep(s3)
            print("The dealer has {} points.".format(d_points))
            sleep(s2)
            break
        else:
            if first_time:
                print("The dealer has {} points.".format(d_points))
                sleep(s2)
                first_time = False
            else:
                print("Now the dealer has {} points.".format(d_points))
                sleep(s2)
            new_card = deck[0]
            print("The dealer dealt himself a {}.".format(new_card[1].upper()))
            sleep(s2)
            hand.append(new_card)
            deck.remove(new_card)
    if d_points > 21:
        print("The dealer busted, you win! Want to play again?")
        sleep(s2)
        main()
    else:
        return d_points


def stay(p_hand, d_hand, deck):
    for card in p_hand:
        if card[0] == 1:
            value_determined = False
            while not value_determined:
                value_determined = True
                print("Would you like your {} to be 1 point or 11 points?".format(card[1]))
                end_value = input()
                if end_value in ["1", "11"]:
                    end_value = int(end_value)
                    card.append(end_value)
                    determine_player_points(p_hand)
                else:
                    print("Please enter only a '1' or an '11'")
                    value_determined = False
    game_over, p_points = determine_player_points(p_hand)
    if not game_over:
        print("You have:")
        new_hand = []
        for card in p_hand:
            name = card[1].upper()
            new_hand.append(name)
        print(", ".join(new_hand))
        sleep(s2)
        print("You have {} points".format(p_points))
        sleep(s2)
        print("The dealer was dealt a(n) {} and a(n) {}".format(d_hand[0][1].upper(), d_hand[1][1].upper()))
        sleep(s3)
        print("Now the dealer will play his hand:")
        sleep(s3)
        d_points = hit_dealer(d_hand, deck)
        sleep(s2)
        compare_points(p_points, d_points)


def compare_points(p_points, d_points):
    if p_points == d_points:
        print("You and the dealer tied with {} points each.".format(p_points))
        sleep(s2)
        print("Want to play again?")
        sleep(s2)
        main()
    elif p_points > d_points:
        print("You had {} points, and the dealer only got {} points. You win!".format(p_points, d_points))
        sleep(s2)
        print("Want to play again?")
        sleep(s2)
        main()
    else:
        print("You had {} points, but the dealer got {} points. You lost.".format(p_points, d_points))
        sleep(s2)
        print("Want to play again?")
        sleep(s2)
        main()

needs_explain = True
main()