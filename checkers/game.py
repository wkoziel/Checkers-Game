import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from .board import Board
class Game:

    #
    def __init__(self, window):
        self._init()
        self.window = window

    #Rysowanie/odświeżanie planszy
    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    #Inicjalizacja nowej gry
    def _init(self):
        self.selected_piece = None;
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()
        
    #Reset gry
    def reset(self):
        self._init()
    
    #Wybieranie pionka - sprawdzanie poprawności wyboru
    def select(self, row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False


    #Przemieszczanie pionków
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    #Zmiana strony z możliwością ruchu
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn == WHITE
        else:
            self.turn = RED
