
import pygame
import sys
from pygame.locals import *
import random
import login



class Card(pygame.sprite.Sprite):

    def __init__(self,number,flower):
        pygame.sprite.Sprite.__init__(self)
        self.flower = flower
        self.number = number
        file_name = "%s%02d" % (flower,number)
        self.card_image = pygame.image.load("cards\\%s.jpg" % file_name).convert_alpha()
        self.back_image = pygame.image.load("cards\\back.jpg").convert_alpha()
        self.real_image = self.card_image

    def setRect(self,rect):
        self.rect = rect
        self.image = pygame.transform.scale(self.real_image ,(rect.width,rect.height))

    def update(self):
        pass

    def __str__(self):
        return "%s%02d" % (self.flower,self.number)


class CardStack:

    def __init__(self):
        self.cardsList = []
        for i in range(1,14):
            self.cardsList.append(Card(i,'A'))
            self.cardsList.append(Card(i,'B'))
            self.cardsList.append(Card(i,'C'))
            self.cardsList.append(Card(i,'D'))
        self.reset()
    def __str__(self):
        s = ''
        for c in self.cardsList:
            s+=str(c) + ' '
        return s
    def reset(self):
        random.shuffle(self.cardsList)
        self.nextIndex = 0

    def getNext(self):
        c = self.cardsList[self.nextIndex]
        self.nextIndex+=1
        return c

class Player:

    def __init__(self,name,cardstack,level):
        self.name = name
        self.score = 0
        self.cards = []
        self.cardstack = cardstack
        self.hit()
        self.hit()
        self.calculateScore()

        self.aiLevel=level # l 2 3


    def continueHit(self):
        if self.aiLevel == 1:
            return len(self.cards)<4
        elif self.aiLevel == 2:
            return self.score <15
        elif self.aiLevel == 3:
            return self.score <17
        else:
            pass

    def hit(self):
        self.cards.append(self.cardstack.getNext())
        self.calculateScore()

    def calculateScore(self):
        self.score = 0
        aceNum = 0
        for c in self.cards:
            self.score+=10 if c.number > 10 else c.number
            if c.number == 1:
                aceNum+=1
        if aceNum == 1 and self.score + 10 <= 21:
            self.score+=10

    def __str__(self):
        s = "%s(%d):  " % (self.name,self.score)
        for c in self.cards:
            s+=str(c) + ' '
        return s

if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((900,600),0,32)

    stack = CardStack()
    player = Player("A",stack)
    player.hit()
    print(player)
    player.hit()
    print(player)
    player.hit()
    print(player)
    player.hit()
    print(player)
    player.hit()
    print(player)
    player.hit()
    print(player)

