# Alvee Alamgir
# eq_read_file.py
# Show equalizer based on values read from a file
## Currently very small and simple, set up for hardware

# importing required libraries (mainly pygame)
import pygame, sys
from pygame.locals import *     
from random import *

pygame.init();
fpsClock = pygame.time.Clock()  # set a max FPS rate

# Some random colours
redCol = pygame.Color(255,0,0)
greenCol = pygame.Color(0,255,0)
blueCol = pygame.Color(0,0,255)
yellowCol = pygame.Color(255,255,0)
purpleCol = pygame.Color(255,0,255)
tealCol = pygame.Color(0,255,255)
orangeCol = pygame.Color(255,128,0)

screen = pygame.display.set_mode((500,410)) #height,width
pygame.display.set_caption('Super Salad?')

screen.fill(pygame.Color(255,255,255))

# File with band frequencies written to it
valFile = open('band_values.txt','r')   

# At this point a class isn't required but will allow for effects in the future
# A class for the frequency bands
class freqBand:
    oldVal = 0
    value = 0
    boxRect = []
    startPos = 0
    
    
    def __init__(self, startX):
        self.value = 0
        self.startPos = startX
        self.boxRect = []
        for i in range(0,10):
            self.boxRect.append(Rect(self.startPos,370-40*i,60,30))

    def drawBoxes():
        for box in boxRect:
            pygame.draw.rect(screen,redCol,box)

    def setVal(self,newVal):# store old value. Can be used for effects later
        self.oldVal = self.value
        self.value = newVal

# get what colour to draw depending on value
def setCol(n):
    if (n < 6):
        return pygame.Color(0,255,0)
    elif (n >= 6 and n < 8):
        return pygame.Color(255,255,0)
    else:
        return pygame.Color(255,0,0)
        

frequencies = []
for i in range(0,7):
    frequencies.append(freqBand(10+70*i))
      
while True:
    screen.fill(pygame.Color(0,0,0))

    #Get the values from the file
    valLine = valFile.readline().rstrip().split(" ")
    if (len(valLine) != 7):#if end of the file is reached, close pygame
        pygame.quit()
        sys.exit()
        
    for i in range(0,7):
        frequencies[i].setVal(int(valLine[i]))# set band values from file
        for j in range(0,frequencies[i].value):
            pygame.draw.rect(screen,setCol(j),frequencies[i].boxRect[j])
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEMOTION:
            mx,my = event.pos

    pygame.display.update()
    # Adjust later depending on how fast the sampling rate is
    fpsClock.tick(1)   #wait long enough to run at __ fps, call after update


