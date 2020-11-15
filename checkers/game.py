import pygame
from .constants import *
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
        self.turn = WHITE
        self.valid_moves = {}
    

    #Rysowanie/odświeżanie planszy
    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        self.draw_turn(self.window)
        if self.winner() != None:
            self.winner_screen()
        pygame.display.update()


    #Wyświetla informacje na temat ruchu oraz pozostałych pionków
    def draw_turn(self, window):
        info = "Pozostało: " + str(self.board.white_left) + " białych, " + str(self.board.black_left) + " czarnych."
        if self.turn == WHITE:
            text = SMALL_FONT.render(("Ruch BIAŁYCH!       " + info), True, WHITE)
        else:
            text = SMALL_FONT.render(("Ruch CZARNYCH!      " + info), True, WHITE)
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT + 5))


    #Wyświetla wygranego
    def winner_screen(self):
        win = "WYGRYWAJĄ"
        if self.winner() == WHITE:
            win += " BIAŁE!"
        else:
            win += " CZARNE!"
        text = D_FONT.render(win , True, YELLOW)
        reset_info = MEDIUM_FONT.render("Aby zresetowac gre wcisnij r", True, WHITE)
        pygame.draw.rect(self.window, BLACK, (0, 200, 600, 200))
        self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        self.window.blit(reset_info, (WIDTH // 2 - reset_info.get_width() // 2, HEIGHT // 2 - reset_info.get_height() // 2 + 80))


    #Wyświetla ekran powitalny
    def intro_screen(self):
        self.window.fill(WHITE)
        pygame.draw.rect(self.window, ORANGE, (50,50 , 500, 50))
        pygame.draw.rect(self.window, ORANGE, (50,500 , 500, 50))
        pygame.draw.rect(self.window, ORANGE, (50,50 , 50, 450))
        pygame.draw.rect(self.window, ORANGE, (500,50 , 50, 450))

        for i in range (2,10):
          for j in range (2,10):
              if (i%2==0 and j%2==0):  pygame.draw.rect(self.window, BLACK, (i*50+50,j*50 , 50, 50))
              if (i%2==0 and j%2==1):  pygame.draw.rect(self.window, BLACK, (i*50,j*50 , 50, 50))
              
        text = SMALL_FONT.render("Wybierajac spacje zaczniesz nowa gre, aby zresetowac gre wcisnij r", True, BLACK)
        text2 =D_FONT.render("Warcaby", True, BLACK)
        self.window.blit(text, (50, 570))
        self.window.blit(text2, (185, 0))
        

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
