import pygame

#Stałe kolory - RGB
RED = (255, 0, 0)
WHITE = (211, 211, 211)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (125, 125, 125)

#Stałe wielkości używane w programie
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#Obrazy importowane z zewnątrz
CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))