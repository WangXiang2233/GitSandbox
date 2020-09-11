import pygame
from pygame.locals import *
import sys
from enum import Enum

# ####################
# const
# ####################

class MouseStatus(Enum):
    UP = 0
    DONW = 1

BOARD_CELL_SIZE = 8
BOARD_WIDTH = 1024
BOARD_HEIGHT = 640
BOARD_COLUMN_COUNT = int(BOARD_WIDTH / BOARD_CELL_SIZE)
BOARD_ROW_COUNT = int(BOARD_HEIGHT / BOARD_CELL_SIZE)

# ####################
# global 
# ####################

mouseStatus = MouseStatus.UP

# ####################
# sub functions 
# ####################

def init():
    pygame.init()                                               
    pygame.display.set_caption("Game of Life")                          
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))                
    screen.fill((0,0,0))
    for i in range(BOARD_ROW_COUNT+1):
        pygame.draw.line(screen, (0,95,0), (0,BOARD_CELL_SIZE*i), (BOARD_WIDTH,BOARD_CELL_SIZE*i), 1)   
    for i in range(BOARD_COLUMN_COUNT+1):
        pygame.draw.line(screen, (0,95,0), (BOARD_CELL_SIZE*i,0), (BOARD_CELL_SIZE*i,BOARD_WIDTH), 1)   

    pygame.display.update()   
    return screen                              

def locateCellX(x):
    return int(x / BOARD_CELL_SIZE)

def locateCellY(y):
    return int(y / BOARD_CELL_SIZE)

def drawCell(screen, x, y):
    pygame.draw.rect(screen, (0,95,0), pygame.Rect(x*BOARD_CELL_SIZE,y*BOARD_CELL_SIZE,BOARD_CELL_SIZE,BOARD_CELL_SIZE))
    print("mouse moved   -> (" + str(x) + ", " + str(y) + ")")
    pygame.display.update()   

# ####################
# main functions 
# ####################

def main():

    screen = init()

    mouseStatus = MouseStatus.UP

    while (1):
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:                              
                pygame.quit()                                   
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouseStatus = MouseStatus.DONW
                x, y = event.pos
                drawCell(screen, locateCellX(x), locateCellY(y))
            elif event.type == MOUSEBUTTONUP:
                mouseStatus = MouseStatus.UP
                x, y = event.pos
                drawCell(screen, locateCellX(x), locateCellY(y))
            elif event.type == MOUSEMOTION:
                if mouseStatus == MouseStatus.DONW:
                    x, y = event.pos
                    drawCell(screen, locateCellX(x), locateCellY(y))

if __name__ == "__main__":
    main()
