import os
import pygame, sys
from pygame.locals import *
import pygame

# initialize game engine
pygame.init()

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
bright_red = (255,0,0)
bright_green = (0,255,0)


#end of color, go to clock 

clock = pygame.time.Clock()
background_image = pygame.image.load("table.jpg").convert()



#put all image here
card_back=pygame.image.load("back.jpg")
card1=pygame.image.load("h8.jpg")
card2=pygame.image.load("ca.jpg")
card3=pygame.image.load("s3.jpg")
card_player=pygame.image.load("hq.jpg")








while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    pygame.display.flip()
    clock.tick(clock_tick_rate)

    pygame.draw.rect(screen, WHITE , [rect_x,rect_y,rect_width,rect_height])
    rect_x+=animation_increment

 #   def game_intro():
#
 #   	intro = True
#
 #   	while intro:
  #      	for event in pygame.event.get():
   #         	#print(event)
    #       		if event.type == pygame.QUIT:
     #      	 		pygame.display.quit()
            
                
     #   	gameDisplay.fill(white)
      #  	largeText = pygame.font.Font('freesansbold.ttf',115)
   #      	TextRect.center = ((display_width/2),(display_height/2))
 #       	gameDisplay.blit(TextSurf, TextRect)

#
#        	mouse = pygame.mouse.get_pos()

        #print(mouse)

      #  	if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
     #     	 	pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
    #    	else:
   #         	pygame.draw.rect(gameDisplay, green,(150,450,100,50))
  #      		pygame.draw.rect(gameDisplay, red,(550,450,100,50))
 #       		pygame.display.update()
#        		clock.tick(15)


#cards are all below
    backcard=pygame.transform.scale(card_back,(90,110))
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
