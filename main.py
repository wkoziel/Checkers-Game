import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.game import Game

#Wstępna konfiguracja okna gry
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT+30))
pygame.display.set_caption('Warcaby')


#Funkcja zwraca pozycje kursora
def get_position_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

#Ekran powitalny
def intro_loop(clock, game):
    intro = True
    while intro:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                intro = False
        game.intro_screen()
        pygame.display.update()


#Główna pętla gry
def main():
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    intro_loop(clock, game)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(position)
                game.select(row, col)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game.reset()
        game.update()


#INIZJALIZACJA
main()