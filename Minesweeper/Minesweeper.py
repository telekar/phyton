# Minesweeper
#
# Based on Youtube-Series from Graviatar 
# https://github.com/Gravitar64/A-beautiful-code-in-Python
# https://www.youtube.com/watch?v=diuLxpU2pWg&list=PLhC_4AWNg9rnM_qAPyUU4Wo1kJoOAMC6_&index=13&t=955s
#
import pygame as pg
import random as rnd
from dataclasses import dataclass

# Variables
resolution = 800                                                        # auflösung
fields = 25 #int(input("Anzahl Felder: "))                              # raster
distance = resolution // fields                                         # abstand
maxMines  = setMines = 70 #int(input("Anzahl Minen: "))                 # anzMinen
matrix = []
neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]     # benachbarteFelder


# pg setup
pg.init()
screen = pg.display.set_mode([resolution, resolution],pg.RESIZABLE)
pg.display.set_caption('MINESWEEPER')
clock = pg.time.Clock()

cell_normal = pg.transform.scale(pg.image.load("cell_normal.gif"),(distance,distance))
cell_marked = pg.transform.scale(pg.image.load("cell_marked.gif"),(distance,distance))
cell_mine = pg.transform.scale(pg.image.load("cell_mine.gif"),(distance,distance))

cell_selected = []
for n in range(9):
    cell_selected.append(pg.transform.scale(pg.image.load(f"cell_{n}.gif"),(distance,distance)))

@dataclass

class Cell():
    # x and y changed to row and line, because pygame gives coordinates for x from left to right
    # and y from up to down
    row : int  # x
    line : int   # y
    mine : bool = False
    selected : bool = False
    flagged : bool = False
    MinesArround : int = 0

    def show(self):
        pos =(self.row*distance, self.line*distance)
        if self.selected:
            if self.mine:
                screen.blit(cell_mine,pos)
            else:
                screen.blit(cell_selected[self.MinesArround],pos)
        else:
            if self.flagged:
                screen.blit(cell_marked,pos)
            else:
                screen.blit(cell_normal,pos)

    def checkMines(self):
        for pos in neighbors:
            newRow = self.row + pos[0]
            newLine = self.line + pos[1]
            if newLine >= 0 and newLine < fields and newRow >= 0 and newRow < fields:
               if matrix[newRow*fields + newLine].mine:
                   self.MinesArround +=1

def floodFillZero(row,line):
    for pos in neighbors:
        newRow = row + pos[0]
        newLine = line + pos[1]
        if newLine >= 0 and newLine < fields and newRow >= 0 and newRow < fields:
            cell = matrix[newRow*fields + newLine]
            if cell.MinesArround == 0 and not cell.selected:
                cell.selected = True
                floodFillZero(newRow,newLine)
            else:
                cell.selected = True

def countFlagged(matrix):
  counter = 0
  for n in range(fields*fields):
    if matrix[n].flagged:
        counter += 1
  return counter

def countSelected(matrix):
  counter = 0
  for n in range(fields*fields):
    if matrix[n].selected:
        counter += 1
  return counter

#fill matrix
for n in range(fields*fields):
    matrix.append(Cell(n // fields, n % fields))

#set mines
while maxMines > 0:
    x = rnd.randrange(fields*fields)
    if not matrix[x].mine:
        matrix[x].mine = True
        maxMines -=1

#testmines
for object in matrix:
    if not object.mine:
        object.checkMines()

#pg control
running = True

while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouseX , mouseY = pg.mouse.get_pos()
            row = mouseX // distance
            line = mouseY // distance
            idx = row * fields + line
            cell = matrix[idx]
            if pg.mouse.get_pressed()[2]:
                if not cell.selected:
                    cell.flagged = not cell.flagged
                    if countFlagged(matrix) >= 0:
                        pg.display.set_caption(f'MINESWEEPER {setMines - countFlagged(matrix)} Bomben übrig')
                
            if pg.mouse.get_pressed()[0]:
                cell.selected = True
                if cell.MinesArround == 0 and not cell.mine:
                    floodFillZero(row,line)
                if cell.mine:
                    pg.display.set_caption('MINESWEEPER Du hast verloren !! Versuche es nochmal')
                    for object in matrix:
                        object.selected = True

            if countSelected(matrix) + countFlagged(matrix) == fields * fields:
                pg.display.set_caption('MINESWEEPER Glückwunsch - Du hast gewonnen ')
    
    for object in matrix:
        object.show()

    #print(matrix[0])
    pg.display.flip()
pg.quit()