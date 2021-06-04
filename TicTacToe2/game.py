import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
RED = (255, 0, 0)
BG_COLOUR = (28, 170, 156)
LINE_COLOUR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOUR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))
# print(board)

# pygame.draw.line(screen, LINE_COLOUR, (10, 10), (300, 300), 10)
def draw_lines():
    pygame.draw.line(screen, LINE_COLOUR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOUR, (400, 0), (400, 600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            

print(available_square(1, 1))
mark_square(1, 1, 2)
print(available_square(1, 1))

draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()