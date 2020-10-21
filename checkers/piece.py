import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GRAY, CROWN

class Piece:

    PADDING = 10
    OUTLINE = 2

    #Klasa obiektu pionka - pozycja/kolor/
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calculate_position()

    #Funkcja ustalającące pozycje pionków
    def calculate_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #Funkcja zmieniająca pionek na króla
    def make_king(self):
        self.is_king = False

    #Funkcja rysująca pionki na planszy
    def draw_pieces(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.is_king:
            window.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    #Funkcja zmieniająca położenie pionka
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()

    #Reprezentacja obiektu w konsli za pomocą koloru
    def __repr__(self):
        return str(self.color)