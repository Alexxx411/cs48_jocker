import os
import pygame, sys
import time
import random
from pygame.locals import *
import pygame

# initialize game engine
pygame.init()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg,x,y,w,h,ic,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.ellipse(screen, ic,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.ellipse(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    screen.blit(textSurf, [x+(w/10), y+(h/3)])


rect_x=0
rect_y=50
rect_width=50
rect_height=50

window_width=900
window_height=600

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("~~~~~~  JACK BLACK  ~~~~~~")

dead=False

#color here
WHITE=(255,255,255)
red = (200,0,0)
green = (0,200,0)
sky_blue = (20,100,230)
green_bean = (204,232,207)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_sky_blue = (80,100,200)
black = (0,0,0)



#end of color, go to clock 

clock = pygame.time.Clock()
background_image = pygame.image.load("table.jpg").convert()



#put all image here
card_back=pygame.image.load("back.jpg")
card1=pygame.image.load("h8.jpg")
card2=pygame.image.load("ca.jpg")
card3=pygame.image.load("s3.jpg")
card_player=pygame.image.load("hq.jpg")

def game():
    quit()


while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    #pygame.display.flip()
    clock.tick(clock_tick_rate)

    pygame.draw.rect(screen, WHITE , [rect_x,rect_y,rect_width,rect_height])
    rect_x+=animation_increment

    # largeText = pygame.font.Font('freesansbold.ttf',115)
    # pygame.draw.ellipse(screen, WHITE,(50,500,100,50))
    # pygame.draw.ellipse(screen, sky_blue,(400,500,100,50))
    # pygame.draw.ellipse(screen, red,(750,500,100,50))


    # smallText = pygame.font.Font("freesansbold.ttf",20)
    # textSurf, text_01 = text_objects("START!", smallText)
    # screen.blit(textSurf,[60,515])

    # textSurf, text_01 = text_objects("RESTART!", smallText)
    # screen.blit(textSurf,[406,515])

    # textSurf, text_01 = text_objects("QUIT!", smallText)
    # screen.blit(textSurf,[770,515])


    button("START!",50,500,100,50,green_bean,game)
    button(" QUIT!",750,500,100,50,green_bean,game)
    button("STAND!",400,500,100,50,green_bean,game)



    #pygame.display.update()
    #clock.tick(15)






# def game_intro():

#     intro = True

#     while intro:
#         for event in pygame.event.get():
#             print(event)
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
                
        
        
    






#cards are all below
    backcard = pygame.transform.scale(card_back,(90,110))
    screen.blit(backcard,(100,100))

    #card 0 

    card1=pygame.transform.scale(card1,(90,110))
    screen.blit(card1,(300,100))

    card2=pygame.transform.scale(card2,(90,110))
    screen.blit(card2,(500,100))

    card3=pygame.transform.scale(card3,(90,110))
    screen.blit(card3,(700,100))

    card_player=pygame.transform.scale(card_player,(90,110))
    screen.blit(card_player,(420,380))

    pygame.display.flip()
    clock.tick(clock_tick_rate)

    if(rect_x==window_width-rect_width):
        rect_x=0








