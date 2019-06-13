
import pygame
import sys
import time
import login
import db
from pygame.locals import *
from gameobject import Card,CardStack,Player


class Button(pygame.sprite.Sprite):

    last_button_state = 0

    def __init__(self,pos_x,pos_y,text,callback):

        pygame.sprite.Sprite.__init__(self)

        self.text = text
        self.callback = callback
        self.size = (80,40)
        self.image = pygame.Surface(self.size)
        global fontButtonText
        self.image.fill((255,0,0))

        self.text_surf = fontButtonText.render(self.text,True,Color(0,0,255))		

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


def updateScene(player1,player2,cardsGroup,surface):
    global gameState

    cardsGroup.empty()
    for i in range(len(player1.cards)):
        c = player1.cards[i]
        if i == 0:
            if gameState == 'GAMEWAITING':
                c.real_image = c.card_image
            else:
                c.real_image = c.back_image

        c.setRect(Rect((100 + i * 110,100),(80,100)))
        cardsGroup.add(c)

    for i in range(len(player2.cards)):
        c = player2.cards[i]
        c.setRect(Rect((100 + i * 110,250),(80,100)))
        cardsGroup.add(c)

    
    info_surf = fontDarkRed.render(player1.name,True,Color(255,0,255))
    surface.blit(info_surf,(10,120))

    if gameState == 'GAMEWAITING':
        info_surf = fontDarkRed.render('%d' % player1.score,True,Color(255,0,255))
    else:
        info_surf = fontDarkRed.render('?' ,True,Color(255,0,255))
    surface.blit(info_surf,(10,150))

    info_surf = fontDarkRed.render(player2.name,True,Color(255,0,255))
    surface.blit(info_surf,(10,270))
    
    info_surf = fontDarkRed.render('%d' % player2.score,True,Color(255,0,255))
    surface.blit(info_surf,(10,300))


def InitGamestartState():
    global gameState
    global gamePlayername
    global scene_surface,gameMoney
    gameState = 'GAMESTART'
    

def InitGameplayingState():
    global gameState
    global gamePlayername
    global cardStack,computer,player,cardGroup
    gameState = 'GAMEPLAYING'
    cardStack.reset()
    computer = Player("Dealer",cardStack)
    player = Player(gamePlayername,cardStack)
    cardGroup.empty()



def InitGamewaitingState():

    global gameState
    global gamePlayername
    global cardStack,computer,player,cardGroup

    gameState = 'GAMEWAITING'

    # cardStack.reset()
    # computer=Player("Dealer",cardStack)
    # player =Player(gamePlayername,cardStack)
    # cardGroup.empty()

def InitGameoverState():

    

    global gameState
    global scene_surface
    global gameMoney
    global gamePlayername
    global computer,player

    if player.score > 21:
        gameResult = "LOSS"

    elif computer.score > 21:
        gameResult = "WIN"
    elif player.score > computer.score:
        gameResult = "WIN"
    elif player.score < computer.score:
        gameResult = "LOSS"
    else: 
        gameResult = "DRAW"


    gameState = 'GAMEOVER'

    fontReuslt1 = pygame.font.SysFont('arial',40,bold=False,italic=False)
    fontReuslt2 = pygame.font.SysFont('arial',30,bold=False,italic=False)


    scene_surface.fill((0,100,0))

    database = db.DataBase()
    # print(len(database.records))
    for record in database.records:
        if record.username == gamePlayername:
            break
    if gameResult == 'WIN':
        record.winTimes+=1
        record.money+=gameMoney
        scene_surface.blit(fontReuslt1.render("You Win.  Got   $%d" % (gameMoney),True,Color(255,0,0)),(300,100))

    elif gameResult == 'LOSS':
        record.lossTimes+=1
        record.money-=gameMoney
        scene_surface.blit(fontReuslt1.render("You Loss.  Lose $%d" % (gameMoney),True,Color(0,0,255)),(300,100))
    else:
        scene_surface.blit(fontReuslt1.render("Draw" ,True,Color(0,0,255)),(300,100))
    database.writeFile()


    scene_surface.blit(fontReuslt2.render("Money   Ranking   List" ,True,Color(255,255,0)),(80,180))
    # ranking list money
    moneySortList = database.sortByMoney()
    for i in range(len(moneySortList)):
        record = moneySortList[i]
        scene_surface.blit(fontReuslt2.render("%s" % (record.username),True,Color(255,127,0)),(100,220 + i * 40))
        scene_surface.blit(fontReuslt2.render("%d" % (record.money),True,Color(255,127,0)),(200,220 + i * 40))

    scene_surface.blit(fontReuslt2.render("WinTime   Ranking   List" ,True,Color(255,255,0)),(480,180))
    # ranking list winTimes
    wintimesSortList = database.sortByWinTimes()
    for i in range(len(wintimesSortList)):
        record = wintimesSortList[i]
        scene_surface.blit(fontReuslt2.render("%s" % (record.username),True,Color(255,127,0)),(500,220 + i * 40))
        scene_surface.blit(fontReuslt2.render("%d       %d" % (record.winTimes,record.lossTimes),True,Color(255,127,0)),(600,220 + i * 40))







def main():

    global gameState, gameMoney, gamePlayername

    # check for user name
    gamePlayername = "Annoymous"

    login.main()
    if login.gUserName=='':
        print('exit')
        return
    gamePlayername=login.gUserName



    pygame.init()

    # load music
    pygame.mixer.init()
    snd = pygame.mixer.Sound('bk.wav')
    channel = snd.play()

    gameState = 'GAMEPLAYING'   # can be 'GAMESTART' 'GAMEPLAYING' 'GAMEOVER'

    screen = pygame.display.set_mode((900,600),0,32)

    global fontDarkRed
    fontDarkRed = pygame.font.SysFont('arial',18,bold=False,italic=False)
    global fontButtonText
    fontButtonText = pygame.font.SysFont('arial',18,bold=True,italic=False)

    fontWelcone = pygame.font.SysFont('arial',60,bold=False,italic=False)
    fontBet = pygame.font.SysFont('arial',30,bold=False,italic=False)


    
    # load scene surface
    global scene_surface
    scene_size = (900,600)
    scene_surface = pygame.Surface(scene_size,depth=24)



    global cardStack,computer,player,cardGroup
    cardGroup = pygame.sprite.Group()
    cardStack = CardStack()



    ############### init button for gamestart state ###############
    gui_gamestart_group = pygame.sprite.Group()

    def moneyAdd10():
        global gameMoney
        gameMoney+=10	
    btnAdd10 = Button(350,380,"     + 10",moneyAdd10)
    gui_gamestart_group.add(btnAdd10)

    def moneyAdd1():
        global gameMoney
        gameMoney+=1	
    btnAdd1 = Button(450,380,"      + 1",moneyAdd1)
    gui_gamestart_group.add(btnAdd1)

    def moneyMinus10():
        global gameMoney
        if gameMoney - 10 > 0:
            gameMoney-=10	
    btnMinus10 = Button(350,440,"      - 10",moneyMinus10)
    gui_gamestart_group.add(btnMinus10)

    def moneyMinus1():
        global gameMoney
        if gameMoney - 1 > 0:
            gameMoney-=1	
    btnMinus1 = Button(450,440,"      - 1",moneyMinus1)
    gui_gamestart_group.add(btnMinus1)

    btnStart = Button(400,500,"     Start",InitGameplayingState)
    gui_gamestart_group.add(btnStart)

    global suspendTime
    suspendTime = -1

    ############### init button for gameplaying state ###############
    def playerHit():
        global suspendTime
        if suspendTime == -1:
            player.hit()
            if player.score > 21:
                suspendTime = 30
            

    gui_gameplaying_group = pygame.sprite.Group()
    btnHit = Button(200,450,'       Hit',playerHit)
    gui_gameplaying_group.add(btnHit)

    def playerStand():
        global suspendTime

        if suspendTime == -1:
            InitGamewaitingState()

    gameMoney = 30
    btnStand = Button(500,450,'    Stand',playerStand)
    gui_gameplaying_group.add(btnStand)


    ############### init button for gameover state ###############
    gui_gameover_group = pygame.sprite.Group()

    btnContinue = Button(400,500,'  Continue',InitGamestartState)
    gui_gameover_group.add(btnContinue)


    InitGamestartState()



    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT,100)

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == TIMER_EVENT:

                if suspendTime > 0:
                    suspendTime -= 1
                    if suspendTime == 0:
                        suspendTime = -1
                        InitGameoverState()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        if gameState == 'GAMESTART':
            screen.fill((0,50,50))

            scene_surface.fill(Color(100,100,255))
            scene_surface.blit(fontWelcone.render("Welcome, %s" % (gamePlayername),True,Color(255,0,0)),(250,100))
            scene_surface.blit(fontBet.render("Bet :   %d" % (gameMoney),True,Color(100,255,0)),(370,300))

            gui_gamestart_group.draw(scene_surface)
            gui_gamestart_group.update()

            screen.blit(scene_surface,(0,0))
            pygame.display.update()
        elif gameState == 'GAMEPLAYING':

            screen.fill((0,50,50))
            scene_surface.fill((0,200,0))
            updateScene(computer,player,cardGroup,scene_surface)

            cardGroup.draw(scene_surface)
            gui_gameplaying_group.draw(scene_surface)
            gui_gameplaying_group.update()

            screen.blit(scene_surface,(0,0))
            pygame.display.update()
            if suspendTime == -1 :
                if player.score > 21:				
                    suspendTime = 30
            
        elif gameState == 'GAMEWAITING':			
            # print('e')
            screen.fill((0,50,50))
            scene_surface.fill((0,200,0))
            if suspendTime == -1 :
                computer.hit()

            updateScene(computer,player,cardGroup,scene_surface)
            cardGroup.draw(scene_surface)
            gui_gameplaying_group.draw(scene_surface)

            screen.blit(scene_surface,(0,0))
            pygame.display.update()
            if suspendTime == -1 :
                if computer.score >= 17:
                    suspendTime = 30
                else:
                    time.sleep(0.5)

        elif gameState == 'GAMEOVER':
            screen.fill((0,50,50))
            gui_gameover_group.draw(scene_surface)

            gui_gameover_group.update()
            screen.blit(scene_surface,(0,0))
            pygame.display.update()
        else:
            pass


if __name__ == '__main__':
    main()





