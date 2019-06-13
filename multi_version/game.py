VERSION = 1


import pygame
import sys
import time
import random
import login
import db
from pygame.locals import *
from gameobject import Card,CardStack,Player


class SharedData:

    def __init__(self):
        self.gameState=0
        self.gameMoney=0
        self.gamePlayername=0
        self.gameResult=0
        self.screen=0

        self.fontDarkRed=0
        self.fontButtonText=0
        self.gameplayingBkImage=0
        self.gameBetBkImage=0


        self.cardGroup=0
        self.cardStack=0
        self.computer=0
        self.player=0        
        self.playerList=[0,0,0,0,0] # dock person ai1 ai2 ai3


        self.ticks = 0
        self.gameNextPlayer=0
        self.gameCurrentlayer=1
        self.gameStartTicks=0

        self.gui_gameplaying_group = 0
        self.playerInfo=[1,1,0,0,0]

        self.snd1=0
        self.snd2=0
        self.snd3=0



class Button(pygame.sprite.Sprite):

    last_button_state = 0

    def __init__(self,pos_x,pos_y,text,callback):

        pygame.sprite.Sprite.__init__(self)

        self.text = text
        self.callback = callback
        self.size = (80,40)
        self.image = pygame.Surface(self.size)
        global gameData
        self.image.fill((255,0,0))

        self.text_surf = gameData.fontButtonText.render(self.text,True,Color(0,0,255))		

        self.rect = Rect((pos_x,pos_y),self.size)

    def update(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        mouse_button1,mouse_button2,mouse_button3 = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_x,mouse_y):
            self.image.fill((255,0,0))
            self.image.blit(self.text_surf,(0,10))
            if self.last_button_state == 1 and mouse_button1 == 0:
                self.callback()
                # print("Click",end='')
        else:
            self.image.fill((255,255,0))
            self.image.blit(self.text_surf,(0,10))
        self.last_button_state = mouse_button1


def updateGamePlayingScene():

    global gameData
    gameData.screen.fill((0,0,0))
    gameData.screen.blit(gameData.gameplayingBkImage,(0,0))
    gameData.cardGroup.empty()

    # draw a rect to current player
    pygame.draw.rect(gameData.screen, Color(255,127,0),Rect((90,12 + 120 * gameData.gameCurrentlayer),( 1100, 120)), 3)
    



    for cpuIndex in range(len(gameData.playerList)):

        if gameData.playerInfo[cpuIndex]==0:
            continue

        player=gameData.playerList[cpuIndex]

        # show name
        surf=gameData.fontDarkRed.render(player.name,True,Color(255,255,255),Color(0,0,0))
        gameData.screen.blit( surf,(10,50 + cpuIndex * 120))

        # show score
        if gameData.gameState == 'GAMEPLAYING' and cpuIndex == 0:
            surf=gameData.fontDarkRed.render('?',True,Color(255,255,255),Color(0,0,0))
            gameData.screen.blit( surf,(10,75 + cpuIndex * 120))
        else:
            surf=gameData.fontDarkRed.render(str(player.score),True,Color(255,255,255),Color(0,0,0))
            gameData.screen.blit( surf,(10,75 + cpuIndex * 120))


        for i in range(len(player.cards)):
            c = player.cards[i]
            if i == 0:
                if gameData.gameState == 'GAMEPLAYING' and cpuIndex == 0:
                    c.real_image = c.back_image
                else:
                    c.real_image = c.card_image

            c.setRect(Rect((100 + i * 110,20 + cpuIndex * 120),(80,100)))
            gameData.cardGroup.add(c)


    gameData.cardGroup.draw(gameData.screen)
    gameData.gui_gameplaying_group.draw(gameData.screen)
    gameData.gui_gameplaying_group.update()




def InitGamestartState():
    global gameData
    gameData.gameState = 'GAMESTART'
    # Music
    gameData.snd2.stop()
    gameData.snd3.stop()
    gameData.snd1.play(loops=-1)
    

def InitGameplayingState():
    global gameData

    # Music
    gameData.snd1.stop()
    if random.randint(1,2) == 1:
        gameData.snd2.play(loops=-1)
    else:
        gameData.snd3.play(loops=-1)

    gameData.gameState = 'GAMEPLAYING'
    gameData.cardStack.reset()

    gameData.player = Player(gameData.gamePlayername,gameData.cardStack,1)
    gameData.playerList[0] = Player("Dealer",gameData.cardStack,3)
    gameData.playerList[1] = Player(gameData.gamePlayername,gameData.cardStack,1)

    gameData.playerList[2] = Player("Player 1",gameData.cardStack,gameData.playerInfo[2])
    gameData.playerList[3] = Player("Player 2",gameData.cardStack,gameData.playerInfo[3])
    gameData.playerList[4] = Player("Player 3",gameData.cardStack,gameData.playerInfo[4])

    
    gameData.cardGroup.empty()

    # gameData.playerList[1].hit()
    # gameData.playerList[1].hit()
    # gameData.playerList[1].hit()






def InitGameoverState():

    global gameData

    fontReuslt1 = pygame.font.SysFont('arial',40,bold=False,italic=False)
    fontReuslt2 = pygame.font.SysFont('arial',30,bold=False,italic=False)

    database = db.DataBase()

    
    gameData.gameState = 'GAMEOVER'
    gameData.gameCurrentlayer=1
    gameData.gameNextPlayer=1

    gameData.screen.fill((0,127,0))

    if gameData.playerList[1].score > 21:
        gameData.gameResult = "LOSS"
    else:

        cpuScoreList=[0]
        for i in range(5):        
            if gameData.playerInfo[i] > 0 and i != 1:
                score = gameData.playerList[i].score
                if score > 21:
                    score = 0
                cpuScoreList.append(score)
        maxScore=max(cpuScoreList)

        if gameData.playerList[1].score > maxScore:
            gameData.gameResult = "WIN"
            ratio = 1
            for i in range(2,5):
                if gameData.playerInfo[i]>0:
                    ratio+=1
        elif gameData.playerList[1].score == maxScore:
            # print(str(gameData.playerList[1].score),str(maxScore))
            gameData.gameResult = "DRAW"
        else:
            gameData.gameResult = "LOSS"


    gameData.screen.fill((0,100,0))

    
    # print(len(database.records))
    for record in database.records:
        if record.username == gameData.gamePlayername:
            break
    if gameData.gameResult == 'WIN':
        record.winTimes+=1
        record.money+=gameData.gameMoney*ratio
        gameData.screen.blit(fontReuslt1.render("You Win.  Got $%d x %d" % (gameData.gameMoney, ratio),True,Color(255,0,0)),(400,80))

    elif gameData.gameResult == 'LOSS':
        record.lossTimes+=1
        record.money-=gameData.gameMoney
        gameData.screen.blit(fontReuslt1.render("You Loss.  Lose $%d" % (gameData.gameMoney),True,Color(0,0,255)),(400,80))
    else:
        gameData.screen.blit(fontReuslt1.render("Game   Draw" ,True,Color(0,0,255)),(400,80))
    database.writeFile()


    gameData.screen.blit(fontReuslt1.render("Money Ranking" ,True,Color(255,255,0)),(80,180))
    gameData.screen.blit(fontReuslt2.render("Money   Ranking" ,True,Color(0,255,255)),(100,240))
    # ranking list money
    moneySortList = database.sortByMoney()
    for i in range(len(moneySortList)):
        record = moneySortList[i]
        gameData.screen.blit(fontReuslt2.render("%s" % (record.username),True,Color(255,127,0)),(100,280 + i * 40))
        gameData.screen.blit(fontReuslt2.render("%d" % (record.money),True,Color(255,127,0)),(200,280 + i * 40))

    gameData.screen.blit(fontReuslt1.render("WinTime Ranking" ,True,Color(255,255,0)),(700,180))
    gameData.screen.blit(fontReuslt2.render("Name  Wintimes  Losetimes" ,True,Color(0,255,255)),(720,240))

    # ranking list winTimes
    wintimesSortList = database.sortByWinTimes()
    for i in range(len(wintimesSortList)):
        record = wintimesSortList[i]
        gameData.screen.blit(fontReuslt2.render("%s" % (record.username),True,Color(255,127,0)),(720,280 + i * 40))
        gameData.screen.blit(fontReuslt2.render("%d           %d" % (record.winTimes,record.lossTimes),True,Color(255,127,0)),(860,280 + i * 40))




def getNextPlayer():

    global gameData
    if gameData.gameCurrentlayer >= 1:
        i=2
        while i<5:
            if i>gameData.gameCurrentlayer and gameData.playerInfo[i]>0:
                break
            i+=1
        if i==5:
            i=0
        return i
    if gameData.gameCurrentlayer == 0:
        return -1


def main():


    

    global gameData
    gameData=SharedData()

    pygame.init()

    # load music
    pygame.mixer.init()
    gameData.snd1 = pygame.mixer.Sound('1.ogg')
    gameData.snd2 = pygame.mixer.Sound('2.ogg')
    gameData.snd3 = pygame.mixer.Sound('3.ogg')




    # check for user name
    gameData.gamePlayername = "Amy"
    gameData.gameState = 'GAMEPLAYING'   # can be 'GAMESTART' 'GAMEPLAYING' 'GAMEOVER' 'GAMEWAITING' 'GAMECPU'

    login.main()
    if login.gUserName=='':
        print('exit')
        return
    gamePlayername=login.gUserName


    
    gameData.screen = pygame.display.set_mode((1200,700),0,32)

    
    gameData.fontDarkRed = pygame.font.SysFont('arial',22,bold=False,italic=False)    
    gameData.fontButtonText = pygame.font.SysFont('arial',18,bold=True,italic=False)

    fontWelcone = pygame.font.SysFont('arial',60,bold=False,italic=False)
    fontBet = pygame.font.SysFont('arial',30,bold=False,italic=False)

    
    gameData.gameplayingBkImage = pygame.transform.scale(pygame.image.load("table.jpg").convert_alpha() ,(1200,700))
    gameData.gameBetBkImage = pygame.transform.scale(pygame.image.load("bet.jpg").convert_alpha() ,(1200,700))


    gameData.cardGroup = pygame.sprite.Group()
    gameData.cardStack = CardStack()



    ############### init button for gamestart state ###############
    gui_gamestart_group = pygame.sprite.Group()

    def moneyAdd10():
        global gameData
        gameData.gameMoney+=10	
    btnAdd10 = Button(800-300*(1-VERSION),380,"     + 10",moneyAdd10)
    gui_gamestart_group.add(btnAdd10)

    def moneyAdd1():
        global gameData
        gameData.gameMoney+=1	
    btnAdd1 = Button(900-300*(1-VERSION),380,"      + 1",moneyAdd1)
    gui_gamestart_group.add(btnAdd1)

    def moneyMinus10():
        global gameData
        if gameData.gameMoney - 10 > 0:
            gameData.gameMoney-=10	
    btnMinus10 = Button(800-300*(1-VERSION),440,"      - 10",moneyMinus10)
    gui_gamestart_group.add(btnMinus10)

    def moneyMinus1():
        global gameData
        if gameData.gameMoney - 1 > 0:
            gameData.gameMoney-=1	
    btnMinus1 = Button(900-300*(1-VERSION),440,"      - 1",moneyMinus1)
    gui_gamestart_group.add(btnMinus1)

    btnStart = Button(850-300*(1-VERSION),500,"     Start",InitGameplayingState)
    gui_gamestart_group.add(btnStart)

    if VERSION == 1:

        #######################################################################################
        def player1_0():
            gameData.playerInfo[2]=0
        gui_gamestart_group.add(Button(250,300,"   remove",player1_0))

        def player1_1():
            gameData.playerInfo[2]=1
        gui_gamestart_group.add(Button(350,300,"     easy",player1_1))

        def player1_2():
            gameData.playerInfo[2]=2
        gui_gamestart_group.add(Button(450,300,"   midium",player1_2))

        def player1_3():
            gameData.playerInfo[2]=3
        gui_gamestart_group.add(Button(550,300,"     hard",player1_3))

        #######################################################################################
        def player2_0():
            gameData.playerInfo[3]=0
        gui_gamestart_group.add(Button(250,400,"   remove",player2_0))

        def player2_1():
            gameData.playerInfo[3]=1
        gui_gamestart_group.add(Button(350,400,"     easy",player2_1))

        def player2_2():
            gameData.playerInfo[3]=2
        gui_gamestart_group.add(Button(450,400,"   midium",player2_2))

        def player2_3():
            gameData.playerInfo[3]=3
        gui_gamestart_group.add(Button(550,400,"     hard",player2_3))

        #######################################################################################
        def player3_0():
            gameData.playerInfo[4]=0
        gui_gamestart_group.add(Button(250,500,"   remove",player3_0))

        def player3_1():
            gameData.playerInfo[4]=1
        gui_gamestart_group.add(Button(350,500,"     easy",player3_1))

        def player3_2():
            gameData.playerInfo[4]=2
        gui_gamestart_group.add(Button(450,500,"   midium",player3_2))

        def player3_3():
            gameData.playerInfo[4]=3
        gui_gamestart_group.add(Button(550,500,"     hard",player3_3))




    ############### init button for gameplaying state ###############
    def playerHit():
        global gameData
        if gameData.gameState=='GAMEPLAYING':
            gameData.playerList[1].hit()
            if gameData.playerList[1].score > 21:
                gameData.gameState = "GAMEWAITING"
                gameData.gameStartTicks=gameData.ticks
                gameData.gameCurrentlayer = 1
                gameData.gameNextPlayer = -1
            

    gameData.gui_gameplaying_group = pygame.sprite.Group()
    btnHit = Button(350,630,'       Hit',playerHit)
    gameData.gui_gameplaying_group.add(btnHit)

    def playerStand():
        global gameData
        if gameData.gameState=='GAMEPLAYING':
            # if gameData.playerList[1].score > 21:
            #     pass
            # else
            gameData.gameState = "GAMEWAITING"
            gameData.gameStartTicks=gameData.ticks
            gameData.gameCurrentlayer = 1
            gameData.gameNextPlayer = getNextPlayer()

    gameData.gameMoney = 30
    btnStand = Button(650,630,'    Stand',playerStand)
    gameData.gui_gameplaying_group.add(btnStand)


    ############### init button for gameover state ###############
    gui_gameover_group = pygame.sprite.Group()

    btnContinue = Button(550,600,'  Continue',InitGamestartState)
    gui_gameover_group.add(btnContinue)


    # InitGamestartState()
    InitGamestartState()



    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT,100)

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == TIMER_EVENT:
                gameData.ticks+=1

                # every 100ms


        if gameData.gameState == 'GAMESTART':

            gameData.screen.blit(gameData.gameBetBkImage,(0,0))
            gameData.screen.blit(fontWelcone.render("Welcome, %s" % (gameData.gamePlayername),True,Color(255,0,0)),(450,100))
            gameData.screen.blit(fontBet.render("Bet :   %d" % (gameData.gameMoney),True,Color(100,255,0)),(800-300*(1-VERSION),300))

            if VERSION == 1:  
                tag=['remove','easy','midium','hard']
                gameData.screen.blit(fontBet.render("Player 1:%s" % (tag[gameData.playerInfo[2]]),True,Color(100,255,0)),(20,300))
                gameData.screen.blit(fontBet.render("Player 2:%s" % (tag[gameData.playerInfo[3]]),True,Color(100,255,0)),(20,400))
                gameData.screen.blit(fontBet.render("Player 3:%s" % (tag[gameData.playerInfo[4]]),True,Color(100,255,0)),(20,500))


            gui_gamestart_group.draw(gameData.screen)
            gui_gamestart_group.update()

            # pygame.display.update()
        elif gameData.gameState == 'GAMEPLAYING':

            updateGamePlayingScene()


        elif gameData.gameState == 'GAMEWAITING':   

            updateGamePlayingScene()


            if gameData.gameCurrentlayer == gameData.gameNextPlayer:
                # gap
                if gameData.ticks > gameData.gameStartTicks + 10:
                    gameData.gameState = 'GAMECPU'
            else:
                # change player
                if gameData.ticks > gameData.gameStartTicks + 100:
                    gameData.gameState = 'GAMECPU'
                    gameData.gameCurrentlayer = gameData.gameNextPlayer

                    if gameData.gameNextPlayer == -1:
                        # print("END")
                        InitGameoverState()


        elif gameData.gameState == 'GAMECPU':  

            if gameData.playerList[gameData.gameCurrentlayer].continueHit() == True:
                gameData.playerList[gameData.gameCurrentlayer].hit()
                gameData.gameState = 'GAMEWAITING'
                gameData.gameStartTicks=gameData.ticks
                # gameData.gameCurrentlayer = 1
                # gameData.gameNextPlayer = 0
            else:                

                gameData.gameNextPlayer=getNextPlayer()
                gameData.gameState = 'GAMEWAITING'
                gameData.gameStartTicks=gameData.ticks


            updateGamePlayingScene()

        elif gameData.gameState == 'GAMEOVER':
            # screen.fill((0,50,50))
            gui_gameover_group.draw(gameData.screen)
            gui_gameover_group.update()
            # pygame.display.update()
        else:
            pass

        pygame.display.update()


if __name__ == '__main__':
    main()





