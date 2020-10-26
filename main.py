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
def intro_loop(clock):
    intro = True
    while intro:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            if event.type == pygame.KEYDOWN:
                intro = False
        WINDOW.fill(WHITE)#Tło
        #Piszesz odtąd // Wszsytkie kolory i czcionki są w checkers.constants
        pygame.draw.rect(WINDOW, BLACK, (0,0 , 100, 100))
        text = SMALL_FONT.render("Tekst", True, WHITE)
        WINDOW.blit(text, (0, 0))
        #Dotąd
        pygame.display.update()#To na końcu bo odświeża 

        
#Główna pętla gry
def main():
    clock = pygame.time.Clock()
    intro_loop(clock)
    game = Game(WINDOW)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                row, col = get_position_from_mouse(position)
                game.select(row, col)
        game.update()

#INIZJALIZACJA
main()