import pygame
import time
import signal
import flicklib

@flicklib.flick()
def flick(start,finish):
    global flicktxt
    flicktxt = '' + start[0].upper() + finish[0].upper()
    print(flicktxt)

pygame.init()

gameDisplay = pygame.display.set_mode((800,480))
pygame.display.set_caption('Flick Demo')
a = 1

def disp(x,y):
    gameDisplay.blit(Img, (x,y))

global flicktxt
flicktxt = ''
flickcount = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill((0,0,0))

    if len(flicktxt) > 0 and flickcount < 1:
            flickcount += 1
    else:
            flicktxt = ''
            flickcount = 0

    if flicktxt == 'WE':
        a=a+1

    elif flicktxt == 'EW':
	a=a-1

    if a>5:
	a=1

    elif a<1:
	a=5

    Img = pygame.image.load('fl/'+str(a)+'.jpg')
    disp(0,0)
    #print();
    pygame.display.update()
    #clock.tick(15)
    time.sleep(0.1)

pygame.quit()
quit()
