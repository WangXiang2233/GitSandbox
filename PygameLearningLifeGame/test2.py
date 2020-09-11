import pygame
from pygame.locals import *
import sys
from enum import Enum

# ####################
# const
# ####################

BOARD_CELL_SIZE = 8
BOARD_WIDTH = 1024
BOARD_HEIGHT = 640
BOARD_COLUMN_COUNT = int(BOARD_WIDTH / BOARD_CELL_SIZE)
BOARD_ROW_COUNT = int(BOARD_HEIGHT / BOARD_CELL_SIZE)

# ####################
# class
# ####################

class Board:
    cellsize = BOARD_CELL_SIZE
    width = BOARD_WIDTH
    height = BOARD_HEIGHT
    columns = BOARD_ROW_COUNT
    rows = BOARD_ROW_COUNT

    def init(self):
        pygame.init()                                               
        pygame.display.set_caption("Game of Life")                          
        screen = pygame.display.set_mode((width, height))                
        return screen   

    def draw(self):

# ####################
# global 
# ####################

# todo

# ####################
# sub functions 
# ####################

# ####################
# main functions 
# ####################

def main():

    board = Board()
    screen = board.init()

    while (1):
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
