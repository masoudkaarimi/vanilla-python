import pygame
from sys import exit
from os.path import join

SNAKE_SPEED = 5
NORMAL_APPLE_SCORE = 5
SPECIAL_APPLE_SCORE = 10
LIFETIME_NORMAL = 10
LIFETIME_SPECIAL = 5

ROWS = 10
COLS = 16
CELL_SIZE = 80
STATUS_BAR_HEIGHT = 50
WINDOW_WIDTH = COLS * CELL_SIZE
WINDOW_HEIGHT = ROWS * CELL_SIZE

# colors
LIGHT_GREEN = '#aad751'
DARK_GREEN = '#a2d149'

# start pos 
START_LENGTH = 3
START_ROW = ROWS // 2
START_COL = START_LENGTH + 2

# shadow 
SHADOW_SIZE = pygame.Vector2(4, 4)
SHADOW_OPACITY = 50
