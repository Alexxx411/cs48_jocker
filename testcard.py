import os
import random
import pygame, sys
import time
from pygame.locals import *
import pygame

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

pygame.init()


back=pygame.image.load("back.jpg")
c14=pygame.image.load("ca.jpg")
c2=pygame.image.load("c2.jpg")
c3=pygame.image.load("c3.jpg")
c4=pygame.image.load("c4.jpg")
c5=pygame.image.load("c5.jpg")
c6=pygame.image.load("c6.jpg")
c7=pygame.image.load("c7.jpg")
c8=pygame.image.load("c8.jpg")
c9=pygame.image.load("c9.jpg")
c10=pygame.image.load("c10.jpg")
c13=pygame.image.load("ck.jpg")
c12=pygame.image.load("cq.jpg")
c11=pygame.image.load("cj.jpg")


d14=pygame.image.load("da.jpg")
d2=pygame.image.load("d2.jpg")
d3=pygame.image.load("d3.jpg")
d4=pygame.image.load("d4.jpg")
d5=pygame.image.load("d5.jpg")
d6=pygame.image.load("d6.jpg")
d7=pygame.image.load("d7.jpg")
d8=pygame.image.load("d8.jpg")
d9=pygame.image.load("d9.jpg")
d10=pygame.image.load("d10.jpg")
d13=pygame.image.load("dk.jpg")
d12=pygame.image.load("dq.jpg")
d11=pygame.image.load("dj.jpg")


h14=pygame.image.load("ha.jpg")
h2=pygame.image.load("h2.jpg")
h3=pygame.image.load("h3.jpg")
h4=pygame.image.load("h4.jpg")
h5=pygame.image.load("h5.jpg")
h6=pygame.image.load("h6.jpg")
h7=pygame.image.load("h7.jpg")
h8=pygame.image.load("h8.jpg")
h9=pygame.image.load("h9.jpg")
h10=pygame.image.load("h10.jpg")
h13=pygame.image.load("hk.jpg")
h12=pygame.image.load("hq.jpg")
h11=pygame.image.load("hj.jpg")


s14=pygame.image.load("sa.jpg")
s2=pygame.image.load("s2.jpg")
s3=pygame.image.load("s3.jpg")
s4=pygame.image.load("s4.jpg")
s5=pygame.image.load("s5.jpg")
s6=pygame.image.load("s6.jpg")
s7=pygame.image.load("s7.jpg")
s8=pygame.image.load("s8.jpg")
s9=pygame.image.load("s9.jpg")
s10=pygame.image.load("s10.jpg")
s13=pygame.image.load("sk.jpg")
s12=pygame.image.load("sq.jpg")
s11=pygame.image.load("sj.jpg")

def getcardname(card):
	r=random.randint(1,4)

	if r==1:
		#print ("c")
		i="c"

	if r==2:
		#print ("d")
		i="d"

	if r==3:
		#print ("h")
		i="h"

	if r==4:
		#print ("s")
		i="s"
	cardname = i+str(card)+".jpg"	
	return cardname

def showcard(card,x,y):
	name=getcardname(card)
	print name
	image=pygame.image.load(name).convert()
	image=pygame.transform.scale(image,(90,110))
	screen.blit(image,(x,y))
	pygame.display.update()
	#clock.tick(clock_tick_rate)

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

clock = pygame.time.Clock()
background_image = pygame.image.load("table.jpg").convert()

screen.blit(background_image, [0, 0])
pygame.display.flip()
clock.tick(clock_tick_rate)
showcard("j",400,400)
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

