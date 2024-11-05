# Animation from Lissajous figures
#
# Based on Youtube-Series from Graviatar 
# https://github.com/Gravitar64/A-beautiful-code-in-Python
#
# https://www.youtube.com/playlist?list=PLhC_4AWNg9rklYLWPZmOKeNEW3LcwN5lz
#
# https://de.wikipedia.org/wiki/Lissajous-Figur
#
# also inspired from Daniel Shiffman
# https://www.youtube.com/@TheCodingTrain 
# https://www.youtube.com/watch?v=--6eyLO78CY

import pygame as pg
import math
import time
from dataclasses import dataclass

#variables
resolution = 800
rows = 15
distance = resolution // rows
radius = (distance - 20) // 2
colorDistance = (360//(rows -1))
speed = 0.01
color = pg.Color(0)

#Classes
@dataclass
class Rotor:
    x : int
    y : int
    speed : float
    horizontal : bool
    hue: float
    angle : float = 0
    dotX : int = 0
    dotY : int = 0

    def show(self):
        color.hsva = (self.hue,100,100)
        pg.draw.circle(screen,color,(self.x,self.y),radius,1)   #draw rotor
        pg.draw.circle(screen,(255,255,255),(self.dotX,self.dotY),3)    #draw dot
        if self.horizontal:
            pg.draw.line(screen,(50,50,50),(self.dotX,self.dotY),(self.dotX,resolution))
        else:
            pg.draw.line(screen,(50,50,50),(self.dotX,self.dotY),(resolution,self.dotY))
                         

    def update(self):
        self.angle += self.speed
        self.dotX = int(self.x + radius * math.cos(self.angle))
        self.dotY = int(self.y + radius * math.sin(self.angle))

    def reset(self):
        self.angle = 0

@dataclass
class Lissajous:
    intersections : list
    hue: int

    def show(self):
        if len(self.intersections) > 1:
         color.hsva = (self.hue, 100, 100)
         pg.draw.lines(screen,color,False,self.intersections,1)
         pg.draw.circle(screen,(255,255,255),(self.intersections[-1]),2)  

    def update(self,pos):
        self.intersections.append(pos)

    # Clear the intersection list
    def reset(self):
        self.intersections = []

#define matrix
matrix = [[0]*rows for i in range(rows)]

def setup():
    for n in range(rows):   #create rotors
        x = distance*n + distance // 2
        y = distance // 2
        hue = colorDistance*n
        matrix[0][n] = Rotor(x,y,speed*n,True,hue)   
        matrix[n][0] = Rotor(y,x,speed*n,False,hue)

    for line in range(1,rows):  #create Lissajous
        for row in range(1,rows):
            hue = (matrix[line][0].hue + matrix[0][row].hue) // 2
            matrix[line][row] = Lissajous([],hue)

def draw():
    for n in range(1,rows):
        matrix[0][n].update()
        matrix[n][0].update()

    for line in range(1,rows):
        for row in range(1,rows):
            x = matrix[0][row].dotX
            y = matrix[line][0].dotY
            matrix[line][row].update([x,y])

    for line in range(rows):
        for row in range(rows):
            if line == 0 and row == 0:
                continue
            matrix[line][row].show()

#pg setup
pg.init()
screen = pg.display.set_mode([resolution, resolution])
clock = pg.time.Clock()


setup()

#pg control
running = True

while running:
    clock.tick(20)      #set frame rate
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((0,0,0))
    draw()

#showing
    pg.display.flip()

    #reset lists
    if matrix[0][1].angle > math.pi*2:
        time.sleep(5)
        for row in matrix:
            for objekt in row:
                objekt.reset()
pg.quit()