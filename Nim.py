# Drips
# By Rachel Barrett

# Importing necessary python modules

import pygame, sys, random, math, easygui
from pygame.locals import *

# Constants in the program. Useful as it collects together settings which are arbitrary.

FPS = 30
CAPTION = 'Drips'

WHITE = (255,255,255)
BLUE = (0,128,225)
LIGHTBLUE = (153,204,255)

BGCOLOUR = WHITE
DRIPCOLOUR = BLUE
SELECTEDDRIPCOLOUR = LIGHTBLUE

COLUMNS = 5
ROWS = 8

RADIUS = 20
GAP = 5

BOARDWIDTH = COLUMNS * 2 *(GAP + RADIUS)
BOARDHEIGHT = ROWS * 2 * (GAP + RADIUS)

XMARGIN = 50
YMARGIN = 50

WINDOWWIDTH = BOARDWIDTH + 2 * XMARGIN
WINDOWHEIGHT = BOARDHEIGHT + 2 * YMARGIN


# Main program

def main():
    global DISPLAYSURF, FPSCLOCK

    # Initialising
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption(CAPTION)
    FPSCLOCK = pygame.time.Clock()

    board = random_board(COLUMNS,ROWS)
    mousex = 0
    mousey = 0

    DISPLAYSURF.fill(BGCOLOUR)
    draw_board(board,None)
    #BASICFONT = pygame.font.Font('freesansbold.ttf', 20)
    #DISPLAYSURF.blit(BASICFONT.render('Do you want to go first or second?',True,(0,0,0)),(0,0))
    pygame.display.update()
    #yourturn = easygui.ynbox('do you want to go first or second?','First or second?',('First','Second')) #problematic line
    yourturn = True

    # Main game loop
    while True:

        mouseClicked = False

        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        # Actions dependent on the events

        if sum(board) != 0:
            if yourturn:
                selection = coordinates_to_drip(mousex, mousey)
                if mouseClicked:
                    if selection != None:
                        board[selection[0]] = selection[1]
                        selection = None
                        yourturn = not yourturn
            else:
                selection = None
                pygame.time.wait(1000)
                board = optimal_move(board) 
                yourturn = not yourturn

            DISPLAYSURF.fill(BGCOLOUR)
            draw_board(board,selection)

        # Redraw the screen and wait a clock tick
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Functions called by main

def random_board(x,y):
    return [random.randint(0,y) for i in range(x)]

def draw_board(board,selection):
    for i in range(COLUMNS):
        for j in range(board[i]):
            if selection != None and  i == selection[0] and j >= selection[1]:
                colour = SELECTEDDRIPCOLOUR
            else:
                colour = DRIPCOLOUR
            pygame.draw.circle(DISPLAYSURF,colour,box_center(i,j),RADIUS,0)

def box_center(i,j):
    h = XMARGIN + (GAP + RADIUS) * (1 + 2*i) 
    v = YMARGIN + (GAP + RADIUS) * (1 + 2*j)
    return (h, v)

def coordinates_to_drip(x,y):
    i = (x-XMARGIN)//(2 * (GAP + RADIUS))
    j = (y-YMARGIN)//(2 * (GAP + RADIUS))
    if i in range(COLUMNS) and j in range(ROWS):
        h,v = box_center(i,j)
        if (x-h)**2 + (y-v)**2 <= RADIUS**2:
            return (i,j)
    else:
        return None

def optimal_move(board):

    row = []
    binaryboard = []
    rowsum = 0
    rowsums = []
    remainder = board
    remaindersum = sum(remainder)
    n = 0
    h = 0
    
    while remaindersum != 0:
        row = map(lambda x: x%2,remainder)
        binaryboard.append(row)
        rowsum = sum(row) % 2
        if rowsum == 1:
            h = n
        rowsums.append(rowsum)
        remainder = [(x-y)/2 for x,y in zip(remainder, row)]
        remaindersum = sum(remainder)
        n += 1

    if sum(rowsums) == 0:
        
        i = 0
        while board[i] == 0:
            i += 1
        newboard = board
        newboard[i] = board[i] - 1

    else:
        
        col = 0
        while binaryboard[h][col] == 0:
            col += 1
            
        for i in range(h+1):
            binaryboard[i][col] = (binaryboard[i][col] + rowsums[i]) % 2

        newboard = map(lambda x: int(x,2), map(lambda x: ''.join(map(str,x[::-1])), map(list,zip(*binaryboard))))    

    return newboard

    
# Instruction to run main

if __name__=='__main__':
    main()
                
