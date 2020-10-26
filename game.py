import pygame
from .constants import BLACK, WHITE, GREEN, SQUARE_SIZE, SMALL_FONT, HUGE_FONT, WIDTH, HEIGHT, YELLOW
from .board import Board
class Game:

    #Inicjalizacja nowej gry
    def __init__(self, window):
        self._init()
        self.window = window
    
    #Inicjalizacja nowej gry
    def _init(self):
        self.selected_piece = None;
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}

    
    #Rysowanie/odświeżanie planszy
    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        self.draw_turn(self.window)
        if self.winner() != None:
            self.winner_screen()
        pygame.display.update()


    def draw_turn(self, window):
        info = "Pozostało: " + str(self.board.white_left) + " białych, " + str(self.board.black_left) + " czernych."
        if self.turn == WHITE:
            text = SMALL_FONT.render(("Ruch BIAŁYCH!       " + info), True, WHITE)
        else:
            text = SMALL_FONT.render(("Ruch CZERNYCH!      " + info), True, WHITE)
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT + 5))

    def winner_screen(self):
        win = "WYGRYWAJĄ"
        if self.winner() == WHITE:
            win += " BIAŁE!"
        else:
            win += " CZARNE!"
        text = HUGE_FONT.render(win , True, YELLOW)
        pygame.draw.rect(self.window, BLACK, (0, 200, 600, 200))
        self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        

    #Zwraca zwycięsce parti
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

    #Rysuje kropki na polach na które możemy się ruszyć
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    #Zmiana strony z możliwością ruchu
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK
