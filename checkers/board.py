import pygame
from .constants import BLACK, ROWS, COLS, WHITE, BLACK, SQUARE_SIZE
from .piece import Piece

class Board:

    #Klasa obsługuje rozmieszczenie pionków na planszy
    def __init__(self):
        self.board = []
        self.black_left = 12
        self.white_left = 12
        self.black_kings = 0
        self.white_kings = 0
        self.create_board()


    #Rysowanie szachownicy - kwadratów po których poruszaja się pionki
    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


    #Zmiana pozycji pionków w tablicy
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE and piece.is_king == False:
                self.white_kings += 1
            elif piece.color == BLACK and piece.is_king == False:
                self.black_kings += 1


    #Zwraca pionek jako obiekt
    def get_piece(self, row, col):
        return self.board[row][col]


    #Wypełnianie tablicy board obiektami
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    #Rysowanie planszy
    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_pieces(window)

    #Usuwa pionek z plaszny po biciu
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_left -= 1
                else:
                    self.white_left -= 1


    #Zwraca zwycięsce partii
    def winner(self):
        if self.black_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return BLACK


    #Sprawdza możliwe rucht dla wbranego pionka
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        #Sprawdzanie przekątnych w górę
        if piece.color == BLACK or piece.is_king:
            moves.update(self._side_left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._side_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        #Sprawdzanie przekątnych w dół
        if piece.color == WHITE or piece.is_king:
            moves.update(self._side_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._side_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))

        return moves
    

    #Sprawdza możliwe ruchy na lewo
    def _side_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break   
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._side_left(r + step, row, step, color, left - 1, skipped = last))
                    moves.update(self._side_right(r + step, row, step, color, left + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]              
            left -= 1
        return moves

    #Sprawdza możliwe ruchy na prawo
    def _side_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break    
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._side_left(r + step, row, step, color, right - 1, skipped = last))
                    moves.update(self._side_right(r + step, row, step, color, right + 1, skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves