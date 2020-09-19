import pygame
import sys
import math

from pygame.locals import *
from src.enums.Objects import Objects

# Init env
pygame.init()

GAME_WIDTH = 1000
GAME_HEIGHT = 800

CELL_SIZE = 32
CELL_BORDER_SIZE = 2

GRID = 11

PLAYGROUND_SIZE = GRID * (CELL_SIZE + (CELL_BORDER_SIZE * 2))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (170, 170, 170)

# Fonts
BASIC_FONT = pygame.font.SysFont(None, 32)

# Legend
LEGEND_X = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
LEGEND_Y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

SHOTS_ROWS_COUNT = 10  # Amount of shots in one row
SHOT_SIZE = 25  # Diameter of shot
SHOT_MARGIN = 5  # Distance between shots
SHOTS_MARGIN = 10  # Distance between the playground and shots array


def draw_playground(surface: pygame.Surface, start_x=0, start_y=0, boundaries=False):
    x, y = start_x, start_y

    cell_size_with_border = CELL_SIZE + (CELL_BORDER_SIZE * 2)

    for i in range(0, GRID):  # X
        for j in range(0, GRID):  # Y
            pygame.draw.line(surface, BLACK, (x, y), (x + cell_size_with_border, y), CELL_BORDER_SIZE)  # Top border
            pygame.draw.line(surface, BLACK, (x, y), (x, y + cell_size_with_border), CELL_BORDER_SIZE)  # Left border
            pygame.draw.line(surface, BLACK, (x + cell_size_with_border, y),
                             (x + cell_size_with_border, y + cell_size_with_border),
                             CELL_BORDER_SIZE)  # Right border
            pygame.draw.line(surface, BLACK, (x, y + cell_size_with_border),
                             (x + cell_size_with_border, y + cell_size_with_border),
                             CELL_BORDER_SIZE)  # Bottom border

            if i != 0 and j != 0:
                pygame.draw.rect(surface, GREY,
                                 (x + CELL_BORDER_SIZE, y + CELL_BORDER_SIZE, CELL_SIZE + CELL_BORDER_SIZE,
                                  CELL_SIZE + CELL_BORDER_SIZE))
            else:
                text_str = ''
                if i == 0 and j != 0:
                    text_str = str(LEGEND_Y[j - 1])
                elif i != 0 and j == 0:
                    text_str = LEGEND_X[i - 1]

                text = BASIC_FONT.render(text_str, True, BLACK)
                text_rect: pygame.Rect = text.get_rect()
                text_rect.centerx = x + CELL_BORDER_SIZE + (CELL_SIZE + CELL_BORDER_SIZE) / 2
                text_rect.centery = y + CELL_BORDER_SIZE + (CELL_SIZE + CELL_BORDER_SIZE) / 2

                if text_str:
                    surface.blit(text, text_rect)

            y += cell_size_with_border

        x += cell_size_with_border
        y = start_y

    if boundaries:
        pygame.draw.line(surface, BLUE, (start_x, start_y), (start_x, PLAYGROUND_SIZE), 1)
        pygame.draw.line(surface, BLUE, (start_x, PLAYGROUND_SIZE), (PLAYGROUND_SIZE, PLAYGROUND_SIZE), 1)
        pygame.draw.line(surface, BLUE, (PLAYGROUND_SIZE, start_y), (PLAYGROUND_SIZE, PLAYGROUND_SIZE), 1)
        pygame.draw.line(surface, BLUE, (start_x, start_y), (PLAYGROUND_SIZE, start_y), 1)


def draw_shots(surface: pygame.Surface, amount=20, start_x=0, start_y=0):
    columns_count = math.ceil(amount / SHOTS_ROWS_COUNT)
    start_x = start_x - (columns_count * (SHOT_SIZE + (SHOT_MARGIN * 2))) - SHOTS_MARGIN

    x, y = start_x, start_y

    half_circle = SHOT_SIZE / 2 + SHOT_MARGIN

    for i in range(0, columns_count):
        for j in range(0, SHOTS_ROWS_COUNT):
            pygame.draw.circle(surface, RED, (x + half_circle, y + half_circle), SHOT_SIZE / 2)

            y += SHOT_SIZE + SHOT_MARGIN * 2

        x += SHOT_SIZE + SHOT_MARGIN * 2
        y = start_y


def init():
    playground = []
    shots = 20

    for i in range(0, GRID - 1):
        subfield = []
        for j in range(0, GRID - 1):
            subfield.append(Objects.EMPTY)
        playground.append(subfield)

    # Init window
    window_surface: pygame.Surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), 0, 32)
    pygame.display.set_caption('Battle ship!')

    # Prefill background
    window_surface.fill(WHITE)
    window_rect: pygame.Rect = window_surface.get_rect()

    center_x, center_y = window_rect.centerx, window_rect.centery
    half_playground = PLAYGROUND_SIZE / 2

    draw_playground(window_surface, start_x=center_x - half_playground, start_y=center_y - half_playground)
    draw_shots(window_surface, amount=shots, start_x=center_x - half_playground, start_y=center_y - half_playground)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# Start it
init()
