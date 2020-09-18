import pygame, sys
from pygame.locals import *

# Init env
pygame.init()

# Init window
window_surface: pygame.Surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, World!')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
BASIC_FONT = pygame.font.SysFont(None, 48)

# Texts
text = BASIC_FONT.render('Hello, world!', True, WHITE, BLUE)
text_rect = text.get_rect()
text_rect.centery = window_surface.get_rect().centerx
text_rect.centery = window_surface.get_rect().centery

# Prefill background
window_surface.fill(WHITE)

# Polygon
pygame.draw.polygon(window_surface, GREEN, ((140, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Lines
pygame.draw.line(window_surface, BLUE, (60, 60), (300, 300), 4)
pygame.draw.line(window_surface, BLUE, (350, 270), (76, 76))
pygame.draw.line(window_surface, BLUE, (150, 100), (0, 200), 4)

# Circle
pygame.draw.circle(window_surface, BLUE, (250, 200), 20, 2)

# Ellipse
pygame.draw.ellipse(window_surface, RED, (300, 250, 40, 80), 1)

# Rect
pygame.draw.rect(window_surface, RED,
                 (text_rect.left - 20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40))

# Get array of pixels
pix_array = pygame.PixelArray(window_surface)
pix_array[400][380] = BLACK
del pix_array

# Blit
window_surface.blit(text, text_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
