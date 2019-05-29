import pygame
from pygame.locals import *
import random
import copy


#Global Constants
black = (0,0,0)

white = (255,255,255)
gray = (192,192,192)


back=pygame.image.load("back.jpg")
clubA=pygame.image.load("cA.jpg")
club2=pygame.image.load("c2.jpg")
club3=pygame.image.load("c3.jpg")
club4=pygame.image.load("c4.jpg")
club5=pygame.image.load("c5.jpg")
club6=pygame.image.load("c6.jpg")
club7=pygame.image.load("c7.jpg")
club8=pygame.image.load("c8.jpg")
club9=pygame.image.load("c9.jpg")
club10=pygame.image.load("c10.jpg")
clubK=pygame.image.load("cK.jpg")
clubQ=pygame.image.load("cQ.jpg")
clubJ=pygame.image.load("cJ.jpg")


diamondA=pygame.image.load("dA.jpg")
diamond2=pygame.image.load("d2.jpg")
diamond3=pygame.image.load("d3.jpg")
diamond4=pygame.image.load("d4.jpg")
diamond5=pygame.image.load("d5.jpg")
diamond6=pygame.image.load("d6.jpg")
diamond7=pygame.image.load("d7.jpg")
diamond8=pygame.image.load("d8.jpg")
diamond9=pygame.image.load("d9.jpg")
diamond10=pygame.image.load("d10.jpg")
diamondK=pygame.image.load("dK.jpg")
diamondQ=pygame.image.load("dQ.jpg")
diamondJ=pygame.image.load("dJ.jpg")


heartA=pygame.image.load("hA.jpg")
heart2=pygame.image.load("h2.jpg")
heart3=pygame.image.load("h3.jpg")
heart4=pygame.image.load("h4.jpg")
heart5=pygame.image.load("h5.jpg")
heart6=pygame.image.load("h6.jpg")
heart7=pygame.image.load("h7.jpg")
heart8=pygame.image.load("h8.jpg")
heart9=pygame.image.load("h9.jpg")
heart10=pygame.image.load("h10.jpg")
heartK=pygame.image.load("hK.jpg")
heartQ=pygame.image.load("hQ.jpg")
heartJ=pygame.image.load("hJ.jpg")


spadeA=pygame.image.load("sA.jpg")
spade2=pygame.image.load("s2.jpg")
spade3=pygame.image.load("s3.jpg")
spade4=pygame.image.load("s4.jpg")
spade5=pygame.image.load("s5.jpg")
spade6=pygame.image.load("s6.jpg")
spade7=pygame.image.load("s7.jpg")
spade8=pygame.image.load("s8.jpg")
spade9=pygame.image.load("s9.jpg")
spade10=pygame.image.load("s10.jpg")
spadeK=pygame.image.load("sK.jpg")
spadeQ=pygame.image.load("sQ.jpg")
spadeJ=pygame.image.load("sJ.jpg")

cards = [ diamondA, clubA, heartA, spadeA, \
          diamond2, club2, heart2, spade2, \
          diamond3, club3, heart3, spade3, \
          diamond4, club4, heart4, spade4, \
          diamond5, club5, heart5, spade5, \
          diamond6, club6, heart6, spade6, \
          diamond7, club7, heart7, spade7, \
          diamond8, club8, heart8, spade8, \
          diamond9, club9, heart9, spade9, \
          diamond10, club10, heart10, spade10, \
          diamondJ, clubJ, heartJ, spadeJ, \
          diamondQ, clubQ, heartQ, spadeQ, \
          diamondK, clubK, heartK, spadeK ]
cardA = [ diamondA, clubA, heartA, spadeA ]
card2 = [ diamond2, club2, heart2, spade2 ]
card3 = [ diamond3, club3, heart3, spade3 ]
card4 = [ diamond4, club4, heart4, spade4 ]
card5 = [ diamond5, club5, heart5, spade5 ]
card6 = [ diamond6, club6, heart6, spade6 ]
card7 = [ diamond7, club7, heart7, spade7 ]
card8 = [ diamond8, club8, heart8, spade8 ]
card9 = [ diamond9, club9, heart9, spade9 ]
card10 = [ diamond10, club10, heart10, spade10, \
            diamondJ, clubJ, heartJ, spadeJ, \
            diamondQ, clubQ, heartQ, spadeQ, \
            diamondK, clubK, heartK, spadeK ]

def getAmt(card):
    ''' Returns the amount the card is worth.
E.g. Ace is default 11. 10/Jack/Queen/King is 10.'''
    if card in cardA:
        return 11
    elif card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    else:
        print 'getAmt broke'
        exit()

def genCard(cList, xList):
    '''Generates an card from cList, removes it from cList, and appends it to xList.
Returns if card is Ace and the card itself.'''
    cA = 0
    card = random.choice(cList)
    cList.remove(card)
    xList.append(card)
    if card in cardA:
        cA = 1
    return card, cA

def initGame(cList, uList, dList):
    '''Generates two cards for dealer and user, one at a time for each.
Returns if card is Ace and the total amount of the cards per person.'''
    userA = 0
    dealA = 0
    card1, cA = genCard(cList, uList)
    userA += cA
    card2, cA = genCard(cList, dList)
    dealA += cA
    card3, cA = genCard(cList, uList)
    userA += cA
    card4, cA = genCard(cList, dList)
    dealA += cA
    return getAmt(card1) + getAmt(card3), userA, getAmt(card2) + getAmt(card4), dealA



def main():
    #Local Variable
    ccards = copy.copy(cards)
    stand = False
    userCard = []
    dealCard = []
    winNum = 0
    loseNum = 0
   
    #Initialize Game
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.mixer.music.load("soundeffect.mp3")
    
    pygame.display.set_caption('Blackjack')
    font = pygame.font.SysFont('arial', 15)
    hitTxt = font.render('Hit', 1, black)
    quitTxt = font.render("Quit",1, black)
    standTxt = font.render('Stand', 1, black)
    restartTxt = font.render('Restart', 4, black)
    gameoverTxt = font.render('GAME OVER', 10, white)
    youwinTxt=font.render('YOU WIN', 10, white)
    youloseTxt=font.render('YOU LOSE', 10, white)
    pushTxt=font.render('PUSH', 10, white)
    userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
    pygame.mixer.music.play(-1,0)

    #Fill Background
    background = pygame.Surface(screen.get_size())
    #background = background.convert()
    #background.fill((80, 150, 15))
    background = pygame.image.load("table.jpg").convert()
    #screen.blit(background, [0, 0])
    hitB = pygame.draw.rect(background, gray, (100, 550, 75, 30))
    standB = pygame.draw.rect(background, gray, (300, 550, 75, 30))
    quitB = pygame.draw.rect(background, gray, (800, 30, 75, 30))
    ratioB = pygame.draw.rect(background, gray, (700, 520, 75, 60))

    #Event Loop
    while True:
        #checks if game is over
        gameover = True if (userSum >= 21 and userA == 0) or len(userCard) == 5 else False
        if len(userCard) == 2 and userSum == 21:
            gameover = True
        elif len(dealCard) == 2 and dealSum == 21:
            gameover = True

        #background needs to be redisplayed because it gets updated
        winTxt = font.render('Wins: %i' % winNum, 1, black)
        loseTxt = font.render('Losses: %i' % loseNum, 1, black)

        #checks for mouse clicks on buttons
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()


            

            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and hitB.collidepoint(pygame.mouse.get_pos()):
                #gives player a card if they don't break blackjack rules
                card, cA = genCard(ccards, userCard)
                userA += cA
                userSum += getAmt(card)
                print 'User has a total: %i' % userSum
                while userSum > 21 and userA > 0:
                    userA -= 1
                    userSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and not gameover and standB.collidepoint(pygame.mouse.get_pos()):
                #when player stands, the dealer plays
                stand = True
                while dealSum < 17:
                    card, cA = genCard(ccards, dealCard)
                    dealA += cA
                    dealSum += getAmt(card)
                    print 'Dealer has a total: %i' % dealSum
                    while dealSum > 21 and dealA > 0:
                        dealA -= 1
                        dealSum -= 10
            elif event.type == pygame.MOUSEBUTTONDOWN and (gameover or stand) and restartB.collidepoint(pygame.mouse.get_pos()):
                #restarts the game, updating scores
                if userSum == dealSum:
                    pass
                elif userSum <= 21 and len(userCard) == 5:
                    winNum += 1
                elif userSum <= 21 and dealSum < userSum or dealSum > 21:
                    winNum += 1
                else:
                    loseNum += 1
                gameover = False
                stand = False
                userCard = []
                dealCard = []
                ccards = copy.copy(cards)
                userSum, userA, dealSum, dealA = initGame(ccards, userCard, dealCard)
                #restartB = pygame.draw.rect(background, (80, 150, 15), (450, 325, 75, 30))
            elif event.type == pygame.MOUSEBUTTONDOWN and not (gameover or stand) and quitB.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        screen.blit(hitTxt, (129, 558))
        screen.blit(standTxt, (321, 558))
        screen.blit(quitTxt,(825,40))
        screen.blit(winTxt, (710, 523))
        screen.blit(loseTxt, (710, 548))

        #displays dealer's cards
        for card in dealCard:
            x = 100 + dealCard.index(card) * 110
            card=pygame.transform.scale(card,(90,110))
            screen.blit(card, (x, 100))
        back=pygame.image.load("back.jpg")
        back=pygame.transform.scale(back,(90,110))
        screen.blit(back, (210, 100))

        #displays player's cards
        for card in userCard:
            x = 100 + userCard.index(card) * 110
            card=pygame.transform.scale(card,(90,110))
            screen.blit(card, (x, 300))

        #when game is over, draws restart button and text, and shows the dealer's second card
        if gameover or stand:
        	screen.blit(gameoverTxt, (475, 520))
        	restartB = pygame.draw.rect(background, gray, (470, 550, 75, 30))
        	screen.blit(restartTxt, (480, 555))
        	screen.blit(pygame.transform.scale(dealCard[1],(90,110)), (210, 100))
        	if userSum == dealSum:
        		screen.blit(pushTxt, (475, 500))
        	elif userSum <= 21 and len(userCard) == 5:
        		screen.blit(youwinTxt, (475, 500))
        	elif userSum <= 21 and dealSum < userSum or dealSum > 21:
        		screen.blit(youwinTxt, (475, 500))
        	else:
        		screen.blit(youloseTxt, (475, 500))

        pygame.display.update()
            

if __name__ == '__main__':
    main()
