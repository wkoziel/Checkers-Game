#To jest plik z którego należy uruchamiać aplikacje

import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.board import Board
from checkers.game import Game

#Wstępna konfiguracja
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Warcaby')
FPS = 60

#Funkcja zwraca pozycje kursora
def get_position_from_mouse(position):
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():

    #Inicjalizacja zmiennych
    game = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    #Główna pętla gry
    while game:
        clock.tick(FPS)

        #Pętla nasłuchująca eventy
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(position)
                game.select(row, col)

        #Rysowanie planszy
        game.update()

    pygame.quit()

main()